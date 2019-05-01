Construct a Project instance and get primitive crystal structure info.
```
from casm.project import Project
import os
from os.path import join

# construct a CASM project directory with a ZrO 'prim.json' file
root = join(os.environ["CASM_TEST_PROJECTS_DIR"], "0.3.X", "ZrO" + "_pyex_proj")

# construct a Project
proj = Project(root)

# a casm.project.Prim instance gives info on the primitive crystal structure
prim = proj.prim
print("Lattice (as a column vector matrix):\n", prim.lattice_matrix, "\n")
print("Lattice parameters:\n", prim.lattice_parameters, "\n")
print("Basis coordinate mode:", prim.coordinate_mode, "\n")
print("Basis:")
for b in prim.basis:
    print("-", b)
print("\n")
print("Lattice point group (Schoenflies notation):", prim.lattice_symmetry_s, "\n")
print("Lattice point group (Hermann-Mauguin notation):", prim.lattice_symmetry_hm, "\n")
print("Lattice system name:", prim.lattice_system, "\n")
print("Crystal point group (Schoenflies notation):", prim.crystal_symmetry_s, "\n")
print("Crystal point group (Hermann-Mauguin notation):", prim.crystal_symmetry_hm, "\n")
print("Range of possible space group number:", prim.space_group_number, "\n")
print("Occupational components:", prim.components, "\n")
print("Elements:", prim.elements, "\n")
print("Number of independent compositions:", prim.n_independent_compositions, "\n")
print("Degrees of freedom:", prim.degrees_of_freedom, "\n")

```
<details><summary markdown="span">See result</summary>

```
$ python proj-sec1.1.py
-- Construct: CASM Project -- 
from: "/Users/bpuchala/mcproj/CASM_test_projects/0.3.X/ZrO_pyex_proj"

-- Load project data -- 
read: "/Users/bpuchala/mcproj/CASM_test_projects/0.3.X/ZrO_pyex_proj/.casm/composition_axes.json"

Lattice (as a column vector matrix):
 [[ 3.23398686 -1.61699343 -0.        ]
 [ 0.          2.80071477  0.        ]
 [ 0.          0.          5.16867834]] 

Lattice parameters:
 {'a': 3.23398686, 'b': 3.233986854574291, 'c': 5.16867834, 'alpha': 90.0, 'beta': 90.0, 'gamma': 120.00000005549838} 

Basis coordinate mode: Fractional 

Basis:
- {'coordinate': [0.0, 0.0, 0.0], 'occupant_dof': ['Zr']}
- {'coordinate': [0.6666667, 0.3333334, 0.5], 'occupant_dof': ['Zr']}
- {'coordinate': [0.3333333, 0.6666666, 0.25], 'occupant_dof': ['Va', 'O']}
- {'coordinate': [0.3333333, 0.6666666, 0.75], 'occupant_dof': ['Va', 'O']}


Lattice point group (Schoenflies notation): D6h 

Lattice point group (Hermann-Mauguin notation): 6/mmm 

Lattice system name: hexagonal 

Crystal point group (Schoenflies notation): D6h 

Crystal point group (Hermann-Mauguin notation): 6/mmm 

Range of possible space group number: 191:194 

Occupational components: ['Zr', 'Va', 'O'] 

Elements: ['Zr', 'Va', 'O'] 

Number of independent compositions: 1 

Degrees of freedom: ['occupation']
```
</details>
<br>
