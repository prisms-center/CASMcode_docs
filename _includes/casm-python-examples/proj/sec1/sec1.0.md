Initialize a new CASM project
```
from casm.project import Project
import os
from os.path import join
from shutil import copyfile

# construct a CASM project directory with a ZrO 'prim.json' file
test_dir = os.environ["CASM_TEST_PROJECTS_DIR"]
ZrO_dir = join(test_dir, "0.3.X", "ZrO.0")
pyex_proj_dir = join(test_dir, "0.3.X", "ZrO" + "_pyex_proj")
os.makedirs(pyex_proj_dir)
copyfile(join(ZrO_dir, "prim.json"), join(pyex_proj_dir, "prim.json"))

# list directory contents before 'casm init'
print("Project directory before 'init'")
for file_or_dir in sorted(os.listdir(pyex_proj_dir)):
    print("- " + file_or_dir)

# initialize a new Project
proj = Project.init(pyex_proj_dir)

# list directory contents after 'casm init'
print("Project directory after 'init'")
for file_or_dir in sorted(os.listdir(pyex_proj_dir)):
    print("- " + file_or_dir)

```
<details><summary markdown="span">See result</summary>

```
$ python proj-sec1.0.py
                                                                                                                          Project directory before 'init'
- prim.json
Project directory after 'init'
- .casm
- LOG
- basis_sets
- cluster_expansions
- prim.json
- symmetry
- training_data
```
</details>
<br>
