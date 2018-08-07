Now the `` `casm status -n` `` command shows that a project has been initialized and suggests that the next step is to set composition axes.
```
$ casm status -n
```
<details><summary markdown="span">See result</summary>

```
$ casm status -n

#################################

CASM status:

-- Construct: CASM Project -- 
from: "/Users/bpuchala/Work/codes/CASMcode_v0.2.X_reference/CASM_test_projects/0.3.X/ZrO_tutorial"

-- Load project data -- 
read: "/Users/bpuchala/Work/codes/CASMcode_v0.2.X_reference/CASM_test_projects/0.3.X/ZrO_tutorial/.casm/composition_axes.json"

1) Project initialized: TRUE

- Project name: ZrO
- Project location: /Users/bpuchala/Work/codes/CASMcode_v0.2.X_reference/CASM_test_projects/0.3.X/ZrO_tutorial
- Lattice point group size: 24
- Lattice point group is D6h
- Factor group size: 24
- Crystal point group is: D6h


2) Composition axes 
- Composition axes selected: TRUE



3) Generate configurations 
- Number of supercells generated: 0
- Number of configurations generated: 0
- Number of configurations currently selected: 0

#################################

NEXT STEPS:

Enumerate supercells
- Execute: 'casm enum --method ScelEnum --max V' to enumerate supercells up to 
  volume V (units: number of primitive cells).                            
- Supercells are listed in the SCEL file.
- See 'casm enum --desc ScelEnum' for extended help documentation on how to use the
  '--matrix' and '--lattice-directions' options to perform restricted     
  supercell enumeration (i.e. 2d, 1d, multiples of other supercells).     
- See 'casm format' for a description and location of the  
   'SCEL' file.
```
</details>
<br>
