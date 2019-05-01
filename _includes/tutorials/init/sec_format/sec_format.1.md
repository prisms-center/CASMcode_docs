For a description of the overall CASM project directory structure, use `` `casm format --dir` ``

```
$ casm format --dir
```
<details><summary markdown="span">See result</summary>

```
$ casm format --dir

### dir ##################

  The expected CASM project directory structure with VASP settings  
  files:                                                            
                                                                    
    $ROOT/                                                          
      prim.json                                                     
      (PRIM)                                                        
      LOG                                                           
    $ROOT/.casm                                                     
      project_settings.json                                         
      config_list.json                                              
      composition_axes.json                                         
    $ROOT/symmetry/                                                 
      lattice_point_group.json                                      
      factor_group.json                                             
      crystal_point_group.json                                      
    $ROOT/basis_sets/$CURR_BSET/                                    
      bspecs.json                                                   
      basis.json                                                    
      clust.json                                                    
      $TITLE_Clexulator.*                                           
    $ROOT/training_data/                                            
      SCEL                                                          
    $ROOT/training_data/settings/$CURR_CALCTYPE/                    
      relax.json                                                    
      INCAR                                                         
      SPECIES                                                       
      KPOINTS                                                       
      POSCAR                                                        
    $ROOT/training_data/settings/$CURR_CALCTYPE/$CURR_REF/          
      chemical_reference.json                                       
    $ROOT/training_data/$SCELNAME/                                  
      LAT                                                           
    $ROOT/training_data/$SCELNAME/$CONFIGID                         
      POS                                                           
    $ROOT/training_data/$SCELNAME/$CONFIGID/$CURR_CALCTYPE          
      (VASP/QE results)                                             
      properties.calc.json                                          
    $ROOT/cluster_expansions/clex.formation_energy/$CURR_BSET/$CURR_CALCTYPE/$CURR_REF/$CURR_ECI
      eci.json                                                      
 
 
    Variable descriptions:                                          
 
    $ROOT: root directory of the CASM project                       
 
    $CURR_BSET: Current basis set, by default this is 'bset.default'.
    The current value can be inspected via 'casm settings -l'.      
 
    $CURR_CALCTYPE: Current calctype, by default this is 'calctype.default'.
    The current value can be inspected via 'casm settings -l'.      
 
    $CURR_REF: Current composition axes and reference states, by    
    default this is 'ref.default'. The current value can be inspected
    via 'casm settings -l'.                                         
 
    $SCELNAME: Supercell name, in the form SCELV_A_B_C_D_E_F. 'V' is
    volume of the supercell in terms of the primitive cell, and     
    'A'-'F' are the values of the hermite normal form of the        
    transformation matrix.                                          
 
    $CONFIGID: Configuration id, a unique integer.                  
 
    $TITLE: Title of the CASM project                               

    Note: The 'settings' heirarchy can be located at the project    
    level as shown above, or at the supercell or configuration level
    in order to override calculation, composition, or reference     
    state settings at the supercell or configuration level.  The    
    most local settings are always used for a configuration.
```
</details>
<br>
