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
from: "/Users/bpuchala/mcproj/CASM_test_projects/0.3.X/ZrO_tutorial"

-- Load project data -- 
read: "/Users/bpuchala/mcproj/CASM_test_projects/0.3.X/ZrO_tutorial/.casm/composition_axes.json"

1) Project initialized: TRUE

- Project name: ZrO
- Project location: /Users/bpuchala/mcproj/CASM_test_projects/0.3.X/ZrO_tutorial
- Lattice point group size: 24
- Lattice point group is D6h
- Factor group size: 24
- Crystal point group is: D6h


2) Composition axes 
- Composition axes selected: FALSE


#################################

NEXT STEPS:

Select composition axes
- Execute: 'casm composition -d' to display standard composition axes.    
- Then execute 'casm composition -s <#>' to select one of the listed axes.
- If no standard composition axis is satisfactory, edit the file          
  'composition_axes.json' to add your own custom composition axes to the  
  'custom_axes' JSON object.
- See 'casm format --comp' for description and the location of  
   the 'composition_axes.json' file.
```
</details>
<br>
