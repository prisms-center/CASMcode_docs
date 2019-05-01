Use the Project.command function to execute CASM commands on a particular project
```
from casm.project import Project
import os
from os.path import join

# construct a CASM project directory with a ZrO 'prim.json' file
root = join(os.environ["CASM_TEST_PROJECTS_DIR"], "0.3.X", "ZrO" + "_pyex_proj")

# construct a Project
proj = Project(root)

# select the standard composition axes
returncode = proj.command("composition --select 0")
#print(stdout)

# enumerate supercells
returncode = proj.command("enum -m ScelEnum --max 4")
#print(stdout)

# enumerate configurations
returncode = proj.command("enum -m ConfigEnumAllOccupations --all")
#print(stdout)

```
<details><summary markdown="span">See result</summary>

```
$ python proj-sec2.0.py
-- Construct: CASM Project -- 
from: "/Users/bpuchala/mcproj/CASM_test_projects/0.3.X/ZrO_pyex_proj"

-- Load project data -- 
read: "/Users/bpuchala/mcproj/CASM_test_projects/0.3.X/ZrO_pyex_proj/.casm/composition_axes.json"


***************************

Standard composition axes:

       KEY     ORIGIN          a     GENERAL FORMULA
       ---        ---        ---     ---
         0 Zr(2)Va(2)  Zr(2)O(2)     Zr(2)Va(2-2a)O(2a)
         1  Zr(2)O(2) Zr(2)Va(2)     Zr(2)Va(2a)O(2-2a)

Currently selected composition axes: 0

Parametric composition:
  comp(a) = -0.25*(comp_n(Va) - 2)  + 0.25*comp_n(O) 

Composition:
  comp_n(Zr) = 2
  comp_n(Va) = 2 - 2*comp(a) 
  comp_n(O) = 2*comp(a) 

Parametric chemical potentials:
  param_chem_pot(a) = 2*chem_pot(O) 


Wrote: "/Users/bpuchala/mcproj/CASM_test_projects/0.3.X/ZrO_pyex_proj/.casm/composition_axes.json"

-- Load project data -- 
read: "/Users/bpuchala/mcproj/CASM_test_projects/0.3.X/ZrO_pyex_proj/.casm/composition_axes.json"

-- Begin: ScelEnum -- 
  Generated: SCEL1_1_1_1_0_0_0
  Generated: SCEL2_1_2_1_0_0_0
  Generated: SCEL2_1_2_1_1_0_0
  Generated: SCEL2_1_1_2_0_0_0
  Generated: SCEL3_3_1_1_0_0_1
  Generated: SCEL3_3_1_1_0_0_2
  Generated: SCEL3_1_3_1_2_0_0
  Generated: SCEL3_3_1_1_0_2_2
  Generated: SCEL3_1_1_3_0_0_0
  Generated: SCEL4_1_4_1_0_0_0
  Generated: SCEL4_2_2_1_0_0_1
  Generated: SCEL4_1_4_1_1_0_0
  Generated: SCEL4_4_1_1_0_3_2
  Generated: SCEL4_1_4_1_2_0_0
  Generated: SCEL4_2_2_1_0_1_1
  Generated: SCEL4_2_2_1_0_0_0
  Generated: SCEL4_2_2_1_0_1_0
  Generated: SCEL4_1_2_2_0_0_0
  Generated: SCEL4_1_2_2_1_0_0
  Generated: SCEL4_1_1_4_0_0_0
  DONE.

Write SCEL...
  DONE

Writing config_list...
  DONE
# configurations in this project: 0

-- Begin: ConfigEnumAllOccupations -- 
Enumerate configurations for SCEL1_1_1_1_0_0_0 ...  3 configs.
Enumerate configurations for SCEL2_1_2_1_0_0_0 ...  4 configs.
Enumerate configurations for SCEL2_1_2_1_1_0_0 ...  3 configs.
Enumerate configurations for SCEL2_1_1_2_0_0_0 ...  3 configs.
Enumerate configurations for SCEL3_3_1_1_0_0_1 ...  10 configs.
Enumerate configurations for SCEL3_3_1_1_0_0_2 ...  10 configs.
Enumerate configurations for SCEL3_1_3_1_2_0_0 ...  16 configs.
Enumerate configurations for SCEL3_3_1_1_0_2_2 ...  10 configs.
Enumerate configurations for SCEL3_1_1_3_0_0_0 ...  10 configs.
Enumerate configurations for SCEL4_1_4_1_0_0_0 ...  27 configs.
Enumerate configurations for SCEL4_2_2_1_0_0_1 ...  27 configs.
Enumerate configurations for SCEL4_1_4_1_1_0_0 ...  42 configs.
Enumerate configurations for SCEL4_4_1_1_0_3_2 ...  24 configs.
Enumerate configurations for SCEL4_1_4_1_2_0_0 ...  24 configs.
Enumerate configurations for SCEL4_2_2_1_0_1_1 ...  21 configs.
Enumerate configurations for SCEL4_2_2_1_0_0_0 ...  15 configs.
Enumerate configurations for SCEL4_2_2_1_0_1_0 ...  18 configs.
Enumerate configurations for SCEL4_1_2_2_0_0_0 ...  21 configs.
Enumerate configurations for SCEL4_1_2_2_1_0_0 ...  24 configs.
Enumerate configurations for SCEL4_1_1_4_0_0_0 ...  24 configs.
  DONE.

# new configurations: 336
# configurations in this project: 336

Write SCEL...
  DONE

Writing config_list...
  DONE
```
</details>
<br>
