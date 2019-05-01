{% include tutorials/init/sec4/sec4.2-desc.md %}
```
$ casm composition -d
```
<details><summary markdown="span">See result</summary>

```
$ casm composition -d
-- Construct: CASM Project -- 
from: "/Users/bpuchala/mcproj/CASM_test_projects/0.3.X/ZrO_tutorial"

-- Load project data -- 
read: "/Users/bpuchala/mcproj/CASM_test_projects/0.3.X/ZrO_tutorial/.casm/composition_axes.json"


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
```
</details>
<br>
