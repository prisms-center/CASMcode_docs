"""
Execute the CASM Python examples step-by-step and generate example .md files from the output

Notes:
- There may be multiple examples, which should be included in global var 'python_examples_names'
- Defining examples:
  - Each example is composed of 1 or more sections, and each section of 1 or more steps
  - Each example is summarized in: scripts/casm-python-examples/<example-name>/info.yaml
  - Each section is defined in: scripts/casm-python-examples/<example-name>/<section-name>.yaml
- After running successfully:
  - Each example creates a page: pages/casm-python-examples/<example-name>.md
  - A summary page is created: pages/casm-python-examples.md

"""
from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import *

import yaml
import os
import shutil
import subprocess
import sys
import time
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
        print("Exception in run:", e)
        print("cmd:", cmd)
        print("input:", input)
        print("stdin:", stdin)
        print("encoding:", encoding)
        print("sys.stdout.encoding:", sys.stdout.encoding)
        raise e

# global vars

python_examples_names = [
    "proj"
]

docs_dir = os.environ["CASMcode_docs_DIR"]
test_dir = os.environ["CASM_TEST_PROJECTS_DIR"]
casm_python_examples_dir = join(docs_dir, "scripts", "casm-python-examples")
skip_eval = False
cmd_prefix = "$ "
cwd = "tmp"
if not os.path.exists(cwd):
    os.mkdir(cwd)
env = os.environ.copy()
casm_version=' '.join(run("$CONDA_EXE list | grep 'casm '", env=env, shell=True, executable="/bin/bash")[0].strip().split()[1:3])

def read_yaml(path):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    #print(path + ":\n")
    #print(yaml.dumps(data, indent=2))
    return data

def read_example_info(example_name):
    return read_yaml(join(docs_dir, "scripts", "casm-python-examples", example_name, "info.yaml"))

def read_section(example_name, section_name):
    return read_yaml(join(docs_dir, "scripts", "casm-python-examples", example_name, section_name + ".yaml"))

def eval_cmd(cmd):
    global cwd
    if isinstance(cmd, str):
        display_cmd = cmd_prefix + cmd
        print("(str) cmd:", cmd)

    else:
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
    stdout, stderr, returncode = run(cmd, cwd=cwd, env=env, shell=True, executable="/bin/bash")
    if returncode != 0:
        print("STDOUT:\n", stdout)
        print("STDERR:\n", stderr)
        raise Exception("Command failed:\n" + cmd)
    end = time.time()
    elapsed_time = (end - start)
    return (display_cmd, stdout, stderr, returncode, elapsed_time)


def generate_step(example_name, section_name, step):
    """ Generate _include/casm-python-examples/<example_name>/<section_name>/<step_id>.md"""
    print("    Begin step:", step["id"])
    print("      desc:", step["desc"])

    name = example_name + "-" + step["id"];
    with open(join(cwd, name + ".py"), 'w') as f:
        f.write(step["code"])

    cmd = "python " + name + ".py"
    print("\n        cmd:", cmd)

    display_cmd, stdout, stderr, returncode, elapsed_time = eval_cmd(cmd)
    if returncode:
        print(stdout)
        print(stderr)
        raise Exception("Error running casm c++ example")

    step_result_txt = display_cmd + "\n" + stdout
    print("\n        display_cmd:", display_cmd)
    print("\n        stdout:\n", stdout)
    print("\n        elapsed_time:", elapsed_time)

    # generate step
    path = join(docs_dir, "_includes", "casm-python-examples", example_name, section_name, step["id"] + ".md")
    print("\n      generating:", path)
    with open(join(docs_dir, ".hide", "step_template.md"), 'r') as file :
        filedata = file.read()
    filedata = filedata.replace("PUT_DESC_HERE", step["desc"])
    filedata = filedata.replace("PUT_INPUT_HERE", step["code"])
    filedata = filedata.replace("PUT_RESULT_HERE", step_result_txt.strip())
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file :
        file.write(filedata)
    return

def generate_section(example_name, section):
    """ Execute and generate one section of an example"""
    print("  Begin section:", section["title"])
    section_txt = ""
    for step in section["steps"]:
        generate_step(example_name, section["name"], step)
        # {% include casm-python-examples/example_name/section_name/<step_id>.md %}
        section_txt += "{% include " + join("casm-python-examples", example_name, section["name"], step["id"]+".md") + " %}\n\n"
    return section_txt

def generate_example(example, prev_name=None, next_name=None):
    """ Execuate examples and generate pages/casm-python-examples/<example_name>.md, the individual example page"""
    print("Begin example:", example["name"])
    example_summary = "These examples will show you how to:\n"
    example_txt = ""
    section_i = 1
    for section in example["sections"]:
        section_txt = generate_section(example["name"], section)
        # "### 1. Getting help\n"
        example_txt += "### " + str(section_i) + ". " + section["title"] + "\n\n" + section_txt + "\n"
        example_summary += str(section_i) + ". " + section["summary"] + "\n"
        section_i += 1

    # generate example summary
    path = join(docs_dir, "_includes", "casm-python-examples", "summary_" + example["name"] + ".md")
    print("  generating:", path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(example_summary)

    # generate example page
    path = join(docs_dir, "pages", "casm-python-examples", example["name"] + ".md")
    print("  generating:", path)
    with open(join(docs_dir, ".hide", "casm-python-examples_template.md"), 'r') as file :
        filedata = file.read()
    filedata = filedata.replace("PUT_PYTHON_EXAMPLE_TITLE_HERE", example["title"])
    filedata = filedata.replace("PUT_PYTHON_EXAMPLE_NAME_HERE", example["name"])
    filedata = filedata.replace("PUT_CASM_VERSION_HERE", casm_version)
    filedata = filedata.replace("PUT_PYTHON_EXAMPLE_HERE", example_txt)

    #[Previous](pages/casm-python-examples/<prev>.html) [Up](pages/casm-python-examples.md) [Next](pages/casm-python-examples/<next>.md)
    bottom_nav_txt = ""
    if prev_name is not None:
        bottom_nav_txt += "[[<< Previous]]({{ site.baseurl }}/pages/casm-python-examples/" + prev_name + ".html) "
    bottom_nav_txt += "[[Up]]({{ site.baseurl }}/pages/casm-python-examples.html)"
    if next_name is not None:
        bottom_nav_txt += "[[Next >>]]({{ site.baseurl }}/pages/casm-python-examples/" + next_name + ".html)"
    filedata = filedata.replace("PUT_BOTTOM_NAV_HERE", bottom_nav_txt)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file :
        file.write(filedata)

    return

def generate_index(examples):
    """ Generate pages/casm-python-examples.md, an index of all examples"""
    print("generating pages/casm-python-examples.md")
    return

# Read example specs
examples = []
for example_name in python_examples_names:
    example = read_example_info(example_name)
    example["sections"] = [ read_section(example_name, section_name) for section_name in example["section_names"] ]
    examples.append(example)

# Clear existing any data
# - with a check that target is a grandchild of "CASM_test_projects" before we rmtree
for example in examples:
    if "dir" in example:
        for dir in example["dir"]:
            target = os.path.normpath(os.path.expandvars(dir))
            if os.path.exists(target) and target.split(os.sep)[-3] == "CASM_test_projects":
                shutil.rmtree(target)

# Execute examples and generate pages
example_i = 0
for example in examples:
    if example_i > 0:
        prev_name = python_examples_names[example_i-1]
    else:
        prev_name = None
    if example_i+1 < len(python_examples_names):
        next_name = python_examples_names[example_i+1]
    else:
        next_name = None
    generate_example(example, prev_name, next_name)
    example_i += 1

print(yaml.dump(examples))
generate_index(examples)
