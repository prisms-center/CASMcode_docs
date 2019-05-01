""" Execute the CASM tutorials step-by-step and generate tutorial .md files from the output """
from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import *

import os
import shutil
import subprocess
import sys
import time
import yaml
from os.path import join

def _set_encoding(encoding=None):
    if encoding is None:
        if sys.stdout.encoding is not None:
            return sys.stdout.encoding
        else:
            return 'utf-8'
    else:
        return encoding

def _decode(val, encoding=None):
    try:
        if isinstance(val, bytes):
            return val.decode(_set_encoding(encoding))
        else:
            return val
    except Exception as e:
        print("Exception in prisms_jobs.misc._decode:", e)
        print("val:", val)
        print("sys.stdout.encoding:", sys.stdout.encoding)
        raise e

def run(cmd, input=None, stdin=None, encoding=None, cwd=None, env=None, shell=False, executable=None):
    """Run subprocess and return stdout, stderr as text, returncode as int

    Args:
        cmd (List[str]): Command to run as subprocess
        input (str): Data to be sent to child process
        stdin (stream): Use subprocess.PIPE to pass data via stdin
        encoding (str, optional): Encoding to use to decode stdout, stderr. By
            default, uses sys.stdout.encoding if available, else 'utf-8'.
        cwd (str, optional): Set working directory of subprocess
        env (dict, optional): Environment to use in subprocess
        shell (boolean): Execute cmd using the shell as the executable
        executable (str, optional): Specify the program to execute (can use to replace /bin/sh for shell=True)

    Returns:
        (stdout, stderr, returncode): With stdout and stderr as strings, and
            returncode as int
    """
    try:
        p = subprocess.Popen(cmd, stdin=stdin, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            cwd=cwd, env=env, shell=shell)
        encoding = _set_encoding(encoding)
        if input is not None:
            input = bytearray(input, encoding=encoding)
        stdout, stderr = p.communicate(input=input)
        return (_decode(stdout, encoding), _decode(stderr, encoding), p.returncode)
    except Exception as e:
        print("Exception in prisms_jobs.misc.run:", e)
        print("cmd:", cmd)
        print("input:", input)
        print("stdin:", stdin)
        print("encoding:", encoding)
        print("sys.stdout.encoding:", sys.stdout.encoding)
        raise e

# global vars

tutorial_names = [
    "init",
    "enum"
]

# "enum"
# "calc"
# "bset"
# "learn"
# "monte"
# "phase_diagrams"

docs_dir = os.environ["CASMcode_docs_DIR"]
test_dir = os.environ["CASM_TEST_PROJECTS_DIR"]
tutorials_dir = join(docs_dir, "scripts", "tutorials")
skip_eval = False
cmd_prefix = "$ "
cwd = os.getcwd()
env = os.environ.copy()
casm_version=' '.join(run("$CONDA_EXE list | grep 'casm '", env=env, shell=True, executable="/bin/bash")[0].strip().split()[1:3])

def read_yaml(path):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    #print(path + ":\n")
    #print(yaml.dump(data))
    return data

def write_yaml(path, data):
    with open(path, 'w') as f:
        f.write(yaml.safe_dump(data))

def read_tutorial_info(tutorial_name):
    return read_yaml(join(docs_dir, "scripts", "tutorials", tutorial_name, "info.yaml"))

def read_section(tutorial_name, section_name):
    return read_yaml(join(docs_dir, "scripts", "tutorials", tutorial_name, section_name + ".yaml"))

def read_section_results(tutorial_name, section_name):
    return read_yaml(join(docs_dir, "scripts", "tutorials", tutorial_name, section_name + ".results.yaml"))

def write_section_results(tutorial_name, section_name, section):
    write_yaml(join(docs_dir, "scripts", "tutorials", tutorial_name, section_name + ".results.yaml"), section)

def eval_cmd(cmd):
    global cwd
    if isinstance(cmd, str):
        display_cmd = cmd_prefix + cmd
        print("(str) cmd:", cmd)

    elif isinstance(cmd, dict):
        if "cd" in cmd:
            # {"cd":"<path>"}
            dest = os.path.expandvars(cmd["cd"])
            if not os.path.exists(dest):
                raise Exception("Cannot cd", dest)
            display_cmd = cmd_prefix + "cd " + cmd["cd"]
            os.chdir(dest)
            return (display_cmd, "", "", 0, 0)

        elif "export" in cmd:
            # {"export":"VARIABLE_NAME", "value":"VALUE"}
            env[cmd["export"]] = cmd["value"]
            display_cmd = cmd_prefix + "export " + cmd["export"] + "=" + cmd["value"]
            return (display_cmd, "", "", 0, 0)

    elif isinstance(cmd, list):
        display_cmd = cmd_prefix + ' '.join(cmd)

    if not isinstance(cmd, str):
        raise Exception("Cannot eval:", cmd)

    # run(cmd, input=None, stdin=None, encoding=None)
    #
    # Args:
    #     cmd (List[str]): Command to run as subprocess
    #     input (str): Data to be sent to child process
    #     stdin (stream): Use subprocess.PIPE to pass data via stdin
    #     encoding (str, optional): Encoding to use to decode stdout, stderr. By
    #         default, uses sys.stdout.encoding if available, else 'utf-8'.
    #
    # Returns:
    #     (stdout, stderr, returncode): With stdout and stderr as strings, and
    #         returncode as int

    if skip_eval:
        return (display_cmd, "stdout", "stderr", 0, 0.)

    start = time.time()
    stdout, stderr, returncode = run(cmd, env=env, shell=True, executable="/bin/bash")
    if returncode != 0:
        print("STDOUT:\n", stdout)
        print("STDERR:\n", stderr)
        raise Exception("Command failed:\n" + cmd)
    end = time.time()
    elapsed_time = (end - start)
    return (display_cmd, stdout, stderr, returncode, elapsed_time)


def generate_step(tutorial_name, section_name, step, reuse_results=False):
    """ Generate _include/tutorials/<tutorial_name>/<section_name>/<step_id>.md"""
    print("    Begin step:", step["id"])
    print("      desc:", step["desc"])
    print("step:\n", step)
    step_input_txt = ""
    step_result_txt = ""
    if reuse_results == False:
        step["display_cmd"] = []
        step["stdout"] = []
        step["elapsed_time"] = []
    for i in range(len(step["cmd"])):
        cmd = step["cmd"][i]
        print("\n        cmd:", cmd)
        if reuse_results == False:
            display_cmd, stdout, stderr, returncode, elapsed_time = eval_cmd(cmd)
            step["display_cmd"].append(display_cmd)
            step["stdout"].append(stdout)
            step["elapsed_time"].append(elapsed_time)
        else:
            display_cmd = step["display_cmd"][i]
            stdout = step["stdout"][i]
            elapsed_time = step["elapsed_time"][i]
        step_input_txt += display_cmd + "\n"
        step_result_txt += display_cmd + "\n" + stdout
        print("\n        display_cmd:", display_cmd)
        print("\n        stdout:\n", stdout)
        print("\n        elapsed_time:", elapsed_time)

    # generate step
    path = join(docs_dir, "_includes", "tutorials", tutorial_name, section_name, step["id"] + ".md")
    print("\n      generating:", path)
    with open(join(docs_dir, ".hide", "step_template.md"), 'r') as file :
        filedata = file.read()
    filedata = filedata.replace("PUT_DESC_HERE", step["desc"])
    filedata = filedata.replace("PUT_INPUT_HERE", step_input_txt.strip())
    filedata = filedata.replace("PUT_RESULT_HERE", step_result_txt.strip())
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file :
        file.write(filedata)
    return

def generate_section(tutorial_name, section, reuse_results=False):
    """ Execute and generate one section of a tutorial"""
    print("  Begin section:", section["title"])
    section_txt = ""
    for step in section["steps"]:
        generate_step(tutorial_name, section["name"], step, reuse_results=reuse_results)
        # {% include tutorials/tutorial_name/section_name/<step_id>.md %}
        section_txt += "{% include " + join("tutorials", tutorial_name, section["name"], step["id"]+".md") + " %}\n\n"
    if not reuse_results:
        write_section_results(tutorial_name, section["name"], section)
    return section_txt

def generate_tutorial(tutorial, prev_name=None, next_name=None, reuse_results=False):
    """ Execuate tutorial and generate pages/tutorials/<tutorial_name>.md, the individual tutorial page"""
    print("Begin tutorial:", tutorial["name"])
    tutorial_summary = "This tutorial demonstrates:\n"
    tutorial_txt = ""
    section_i = 1
    for section in tutorial["sections"]:
        section_txt = generate_section(tutorial["name"], section, reuse_results=reuse_results)
        # "### 1. Getting help\n"
        tutorial_txt += "### " + str(section_i) + ". " + section["title"] + "\n\n" + section_txt + "\n"
        tutorial_summary += str(section_i) + ". " + section["summary"] + "\n"
        section_i += 1

    # generate tutorial summary
    path = join(docs_dir, "_includes", "tutorials", "summary_" + tutorial["name"] + ".md")
    print("  generating:", path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(tutorial_summary)

    # generate tutorial page
    path = join(docs_dir, "pages", "tutorials", tutorial["name"] + ".md")
    print("  generating:", path)
    with open(join(docs_dir, ".hide", "tutorial_template.md"), 'r') as file :
        filedata = file.read()
    filedata = filedata.replace("PUT_TUTORIAL_TITLE_HERE", tutorial["title"])
    filedata = filedata.replace("PUT_TUTORIAL_NAME_HERE", tutorial["name"])
    filedata = filedata.replace("PUT_CASM_VERSION_HERE", casm_version)
    filedata = filedata.replace("PUT_TUTORIAL_HERE", tutorial_txt)

    #[Previous](pages/tutorials/<prev>.html) [Up](pages/tutorials.md) [Next](pages/tutorials/<next>.md)
    bottom_nav_txt = ""
    if prev_name is not None:
        bottom_nav_txt += "[[<< Previous]]({{ site.baseurl }}/pages/tutorials/" + prev_name + ".html) "
    bottom_nav_txt += "[[Up]]({{ site.baseurl }}/pages/tutorials.html)"
    if next_name is not None:
        bottom_nav_txt += "[[Next >>]]({{ site.baseurl }}/pages/tutorials/" + next_name + ".html)"
    filedata = filedata.replace("PUT_BOTTOM_NAV_HERE", bottom_nav_txt)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file :
        file.write(filedata)

    return

def generate_index(tutorials):
    """ Generate pages/tutorials.md, an index of all tutorials"""
    print("generating pages/tutorials.md")
    return

# Read tutorial specs:
#
# tutorials: list of dict
# tutorials[i]: dict of <tutorial_name>/info.yaml file contents
#   "title" str, "name" str, "dir" str, "section_names" list of str, "sections": list of dict
# tutorials[i]["sections"][j]: dict of <tutorial_name>/<section_name>.yaml file contents
#   "title" str, "name" str, "summary" str, "steps": list of dict:
# tutorials[i]["sections"][j]["steps"][k]: list of dict:
#   "id": str, "desc": str, "cmd": list of str or dict
# tutorials[i]["sections"][j]["steps"][k]["cmd"]:
#   - if str: execute as command
#   - if dict:
#      - change working directory if: {"cd":"<path>"}
#      - export an environment variable if: {"export":"VARIABLE_NAME", "value":"VALUE"}

reuse_results = True

tutorials = []
for tutorial_name in tutorial_names:
    tutorial = read_tutorial_info(tutorial_name)
    tutorial["sections"] = [ read_section(tutorial_name, section_name) for section_name in tutorial["section_names"] ]
    if reuse_results:
        for i in range(len(tutorial["sections"])):
            section = tutorial["sections"][i]
            section_name = tutorial["section_names"][i]
            results = read_section_results(tutorial_name, section_name)
            for j in range(len(results["steps"])):
                section["steps"][j]["display_cmd"] = results["steps"][j]["display_cmd"]
                section["steps"][j]["stdout"] = results["steps"][j]["stdout"]
                section["steps"][j]["elapsed_time"] = results["steps"][j]["elapsed_time"]
    tutorials.append(tutorial)

# Clear existing any data
# - with a check that target is a grandchild of "CASM_test_projects" before we rmtree
for tutorial in tutorials:
    if "dir" in tutorial:
        for dir in tutorial["dir"]:
            target = os.path.normpath(os.path.expandvars(dir))
            if os.path.exists(target) and target.split(os.sep)[-3] == "CASM_test_projects":
                shutil.rmtree(target)

# Execute tutorials and generate pages
tutorial_i = 0
for tutorial in tutorials:
    if tutorial_i > 0:
        prev_name = tutorial_names[tutorial_i-1]
    else:
        prev_name = None
    if tutorial_i+1 < len(tutorial_names):
        next_name = tutorial_names[tutorial_i+1]
    else:
        next_name = None
    generate_tutorial(tutorial, prev_name, next_name, reuse_results=reuse_results)
    tutorial_i += 1

print(yaml.dump(tutorials))
generate_index(tutorials)
