After completing a calculation, configuration properties are parsed by the Python wrapper and stored in a `` `properties.calc.json` `` file with a standardized format. For a description of this file, use `` `casm format --properties` ``:

```
$ casm format --properties
```
<details><summary markdown="span">See result</summary>

```
$ casm format --properties

### properties.calc.json ##################

properties.calc.json:                                               
  Results of calculations for a particular configuration should be  
  stored in the directory                                           
    $ROOT/training_data/$SCELNAME/$CONFIGID/$CURR_CALCTYPE,         
  and calculated properties summarized in the file                  
    $ROOT/training_data/$SCELNAME/$CONFIGID/$CURR_CALCTYPE/properties.calc.json 
  The 'properties.calc.json' file is read by CASM to extract the    
  first-principles calculted properties of interest. If the         
  'properties.calc.json' file does not exist in the                 
    $ROOT/training_data/$SCELNAME/$CONFIGID/$CURR_CALCTYPE directory
  CASM assumes that no data is available for that configuration.    
  The 'properties.calc.json' uses CASM standard units eV and Angstroms

EXAMPLE:
-------
{
          "atom_type": [
              "A", 
              "B"
          ], 
          "atoms_per_type": [
              1, 
              2
          ], 
          "coord_mode": "direct", 
          "is_complete": true, 
          "relaxed_basis": [
              [0.6666667, 0.6666667, 0.6666667],
              [0.00255632, 0.99488736, 0.00255632],
              [0.33077698, 0.33844594, 0.33077698]
          ], 
          "relaxed_energy": -16.27773537, 
          "relaxed_mag_basis": [
              -3.93,
               3.82,
               1.198
          ], 
          "relaxed_magmom": -1.3086, 
          "relaxed_forces": [
              [0.0, 0.0, 0.0], 
              [0.0, 0.00987362, -0.00987362], 
              [0.0, -0.00987362, 0.00987362]
          ], 
          "relaxed_lattice": [
              [0.0, 1.9174843, 1.9174843], 
              [1.61158655, -1.88219884, 3.79968315], 
              [3.22317311, 0.0, 0.0]
          ]
      }
-------
```
</details>
<br>
