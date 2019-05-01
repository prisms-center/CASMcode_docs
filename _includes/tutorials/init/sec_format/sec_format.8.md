Monte Carlo input files are described by `` `casm format --monte` ``:

```
$ casm format --monte
```
<details><summary markdown="span">See result</summary>

```
$ casm format --monte

### monte ##################

LOCATION WHEN GENERATED:
  User determined


DESCRIPTION:
  The Monte Carlo input file does not need to be in any particular 
  location, as long as it is somewhere inside the CASM project     
  directory or subdirectories. The input file contains a JSON      
  object with "ensemble", "method", "model", "supercell",  
  "data", and "driver" attributes, as described below. An      
  optional attribute "debug" may also be included to print       
  information that may be useful for debugging an input file.      

Input file parameters:                                             

"ensemble" (string):                                             

  Possible options for "ensemble" are:                           

    "GrandCanonical" or "grand_canonical": Semi-grand canonical
    Monte Carlo calculation in which the total number of sites is  
    fixed, but the occupants on each site may vary. One occupant   
    change at a time is attempted.                                 

    "Canonical" or "canonical": Canonical Monte Carlo 
    calculation in which the total number of each type of occupant 
    is fixed. Each Monte Carlo step attempts to swap a pair of     
    occupants.                                                     


"method" (string):                                               

  Possible options for "method" are:                             

    "Metropolis" or "metropolis": Run Monte Carlo calculations 
    using the Metropolis algorithm.                                

    "LTE1" or "lte1": Single spin flip low temperature         
    expansion calculations.                                        


"model": (JSON object)                                           

  /"formation_energy": (string, optional, default="formation_energy")
    Specifies the cluster expansion to use to calculated formation 
    energy. Should be one of the ones listed by 'casm settings -l'.


"supercell": (3x3 JSON arrays of integers)                      
    The supercell transformation matrix.                           

"data": (JSON object)                                            

  /"sample_by": (string)                                         
    Specify unit for the period between samples.  May be either    
    "step" (sample after every "sample_period" proposed Monte  
    Carlo events), or "pass" (sample after the "sample_period" 
    number of passes), where 1 pass is a number of steps equal to  
    the number of sites in the supercell that have variable        
    occupation).                                                   

  /"sample_period": (integer)                                    
    Specify how many steps or passes to wait between data samples. 

  /"measurements": (JSON array containing JSON objects)         
    Specifies which properties to sample. Each JSON object should  
    include "quantity" (string) specifying a property to be      
    sampled. Optionally, it may also include "precision" (number),
    indicating the required (absolute) precision in the average of 
    the quantity for the calculation to be considered converged. If
    a precision is given for any quantity, then the Monte Carlo    
    calculations run in automatic convergence mode and continue    
    until all quantities with a specified precision are converged  
    to level requested.                                            

    Possible options for "quantity" are:                         
      "comp": composition, relative the composition axes         
      "comp_n": composition, number of atoms per unit cell       
      "site_frac": composition, normalized per basis site        
      "atom_frac": composition, normalized per total number of atoms
      "formation_energy": formation energy (per unit cell)       
      "potential_energy": potential energy (per unit cell),      
        (= formation_energy - sum_i(mu_i*comp_i))                  
      "non_zero_eci_correlations": correlations (per unit cell)  
        which have non-zero eci values.                            
      "all_correlations": correlations (per unit cell)           
      "<anything else>": is interpreted as a 'casm query' query  

  /"confidence": (number, range (0.0, 1.0), default 0.95)        
    The confidence level used for calculating the precision in the 
    average value of sampled quantities.                           

  /"min_pass", /"min_step", /"min_sample": (integer)         
    If in automatic convergence mode, prevents the calculation from
    a minimum number of passes, steps, or samples have occurred.   

  /"max_pass", /"max_step", /"max_sample": (integer)         
    If in automatic convergence mode, stops the calculation if the 
    specified number of passes, steps, or samples have occurred.   

  /"N_pass", /"N_step", /"N_sample": (integer)               
    When not in automatic convergence mode (no precision has been  
    specified for any quantities being sampled), stops the         
    calculation when the specified number of passes, steps, or     
    samples have occurred.                                         

  /"equilibration_passes_first_run": (integer)                   
    If included, the requested number of passes will be performed  
    at the initial conditions as a preliminary step before the     
    actual run begins. This may be useful when not running in      
    automatic convergence mode.                                    

  /"equilibration_passes_each_run": (integer)                    
    If included, the requested number of passes will be performed  
    at each condition as a preliminary step before the actual run  
    begins. This may be useful when not running in automatic       
    convergence mode.                                              

  /"storage": (JSON object) Options for writing results.         

    /"output_format": (string or JSON array of string)           
      Specifies the type or types of output files. Current options 
      are "csv" or "json". Type names with either all lower    
      case or all   upper case are accepted.                       

    /"write_observations": (boolean, default false)              
      If true, all individual observations of the quantities       
      requested to be sampled will be written to compressed files: 
        "output_directory"/conditions.i/observations.ext.gz      
      where 'i' is the condition index and 'ext' is the output     
      format.                                                      

    /"write_trajectory": (boolean, default false)                
      If true, the value of all degrees of freedom at the time of  
      each sample will be written to compressed files:             
        "output_directory"/conditions.i/trajectory.ext.gz        
      where 'i' is the condition index and 'ext' is the output     
      format.                                                      

  /"enumeration": (JSON object, optional)                        
    If included, save configurations encountered during Monte      
    Carlo calculations by keeping a 'hall of fame' of best scoring 
    configurations. After the calculation at a particular set of   
    thermodynamic conditions completes, the configurations in the  
    hall of fame are saved to the project configuration list.      

    /"check": (string, default="eq(1,1)")                      
      A 'casm query'-like string that returns a boolean value      
      indicating if (true) a configuration should be considered for
      for the enumeration hall of fame. The default always returns 
      true.                                                        

    /"metric": (string, default="clex_hull_dist(ALL)")         
      A 'casm query'-like string that provides a metric for ranking
      ranking configurations as they are encountered during a Monte
      Carlo calculation. The resulting value is used to create a   
      hall of fame of 'best' configurations encountered during the 
      calculation. When the calculation is complete configurations 
      in the hall of fame are added to the CASM project config     
      list. The 'casm query'-like command should evaluate to a     
      number.                                                      

      Besides the properties listed via 'casm query -h properties',
      and 'casm query -h operators', both "check" and "metric" 
      can also use the property "potential_energy".              

    /"sample_mode": (string, optional, default="on_sample")    
      Indicate when to attempt to insert configurations into the   
      enumeration hall of fame. Options are:                       
        "on_accept": after each accepted Monte Carlo event       
        "on_sample": after each data sample                      

    /"check_existence": (bool, optional, default=true)           
      If true, only configurations that do not already exist in the
      config list are inserted into the enumeration hall of fame.  

    /"insert_canonical": (bool, optional, default=true)          
      If true, configurations are inserted into the enumeration    
      hall of fame in their canonical form. If 'check_existence' is
      true, this must be set to true.                              

    /"N_halloffame": (integer, optional, default=100)            
      The number of configurations that are allowed in the         
      enumeration hall of fame.                                    

    /"tolerance": (number, optional, default=1e-8)               
      Tolerance used for floating point comparison of configuration
      scores in the enumeration hall of fame.                      


"driver": (JSON object)                                          

  /"motif": (JSON object)                                        
      Specifies the initial occupation of the supercell.           

      For canonical ensemble Monte Carlo calculations an additional
      step changes the occupants on random sites to make the actual
      composition as close as possible to the requested composition.

    /"configname": (string, optional)                            
      A configuration name, "auto", "restricted_auto", or      
      "default".                                                 

      Specifies the configuration that is tiled to fill the        
      supercell. If necessary, symmetry operations may be applied  
      An error is thrown if the specified configuration can not be 
      used to fill the "supercell".                              

      Possible options for "configname" are:                     
        A configuration name (ex. "SCEL3_3_1_1_0_2_2/0")         
        "auto": ("grand_canonical" ensemble only) Enumerated   
        configurations will be searched for the configuration with 
        the lowest potential energy to use as the motif.           
        "default": If the value "default" is used, the initial 
        motif occupation is determined from the occupation order in
        the PRIM.                                                  
        "restricted_auto": ("grand_canonical" ensemble only)   
        Same as "auto", but only configurations that can tile the
        supercell are considered. As a last resort, "default" is 
        used.                     

    /"configdof": (string, optional)                             
      Specifies the path to a configdof JSON file, such as         
      "initial_state.json" or "final_state.json", containing   
      the degrees of freedom to initialize the supercell with      

  /"mode": (string)                                              
    Specify the drive mode.                                        

    Possible options for "mode" are:                             
      "incremental": perform one or more calculations, starting  
        at the initial conditions and incrementing by the          
        incremental conditions up to (and including) the final     
        conditions.                                                

      "custom": perform one or more calculations, as specified by
        the "custom_conditions".                                 

  /"dependent_runs": (boolean, default true)                     

    If true, begin the next calculation with the final DoF from the
    previous calculation. If false, begin each calculation with the
    DoF specified for the "motif".

  /"initial_conditions",
  /"incremental_conditions", 
  /"final_conditions": (JSON object, optional)                    
    Specifies the applied conditions for the calculation. For       
    "incremental_conditions", specifies the change in conditions  
    between individual calculations. Each JSON object should        
    include:                                                        

    /"temperature": (number)                                      
      The temperature in K.                                         

    /"param_chem_pot" (JSON object, "grand_canonical" ensemble only)
      The parametric chemical potential(s)                          

      /"a", /"b", ...: (number)                                 
      The parametric chemical potentials conjugate to the parametric
      compositions. The number of parametric chemical potentials    
      provided must match the number of independent compositions.   

    /"comp" (JSON object, "canonical" ensemble only, option 1)
      The parametric composition(s)                          

      /"a", /"b", ...: (number)                                 
      The parametric composition. The number of entries provided    
      must match the number of independent compositions.            

    /"comp" (JSON array, "canonical" ensemble only, option 2)
      The parametric composition(s)                          

      [number, ...]                                                 
      An array containing the parametric composition. The number of 
      entries provided must match the number of independent         
      compositions.                                                 

    /"comp_n" (JSON object, "canonical" ensemble only, option 3)
      The mol composition per unitcell                          

      /"A", /"B", ...: (number)                                 
      The mol composition per unitcell. The entries provided must   
      match occupant names in the 'prim.json' file. The values are  
      summed, normalized, and then converted to parametric composition.

    /"comp_n" (JSON array, "canonical" ensemble only, option 4)
      The mol composition per unitcell                          

      [number, ...]                                                 
      An array containing the mol composition per unitcell. The     
      number of entries provided must match the number components.  
      The values are summed, normalized, and converted to parametric
      composition.  

    /"tolerance": (number)                                        
      Specifies a numerical tolerance for comparing conditions.     

  /"custom_conditions":
    (JSON array of JSON objects) An array specifying a custom     
    path of conditions.                                           

  Restarts: Metropolis Monte Carlo calculations that are stopped   
  before the entire path has been calculated can be restarted as   
  long as the conditions of the existing calculations agree with   
  the conditions specified in the input settings. This means that  
  the "final_conditions" might be changed to increase the length 
  of a path, or additional "custom_conditions" might be added,   
  but the "incremental_conditions" may not be changed. Upon      
  restart, the results summary file is checked for the last        
  finished conditions. Then the path is resumed from the next set  
  of conditions. It is the responsibility of the user to ensure    
  that other important settings, such as the "model" are not     
  changed inappropriately.                                         


"debug" (bool, default false):                                   

  If true, will print as much information as possible to assist in 
  debugging input file settings.                                   


EXAMPLE: Settings for an incremental Metropolis calculation     
with increasing temperature in automatic convergence mode.
-------
{
  "comment" : "This is a sample input file. Unrecognized attributes (like the ones prepended with '_' are ignored.",
  "debug" : false,
  "ensemble" : "grand_canonical",
  "method" : "metropolis",
  "model" : {
    "formation_energy" : "formation_energy"
  },
  "supercell" : [
    [10, 0, 0],
    [0, 10, 0],
    [0, 0, 10]
  ],
  "data" : {
    "sample_by" : "pass",
    "sample_period" : 1,
    "_N_sample" : 1000, 
    "_N_pass" : 1000,
    "_N_step" : 1000,
    "_max_pass" : 10000,
    "min_pass" : 1000,
    "_max_step" : 10000,
    "_max_sample" : 500,
    "_min_sample" : 100,
    "confidence" : 0.95,
    "measurements" : [ 
      { 
        "quantity" : "formation_energy"
      },
      { 
        "quantity" : "potential_energy"
      },
      { 
        "quantity" : "atom_frac"
      },
      { 
        "quantity" : "site_frac"
      },
      { 
        "quantity" : "comp",
        "precision" : 1e-3
      },
      { 
        "quantity" : "comp_n"
      }
    ],
    "storage" : {
      "write_observations" : false,
      "write_trajectory" : false,
      "output_format" : ["csv", "json"]
    }
  },
  "driver" : {
    "mode" : "incremental", 
    "motif" : {
      "configname" : "auto",
      "_configname" : "SCEL3_3_1_1_0_2_2/0",
      "_configdof" : "path/to/final_state.json"
    },
    "initial_conditions" : {
      "param_chem_pot" : {
        "a" : -1.75
      },
      "temperature" : 100.0,
      "tolerance" : 0.001
    },
    "final_conditions" : {
      "param_chem_pot" : {
        "a" : -1.75
      },
      "temperature" : 1000.0,
      "tolerance" : 0.001
    },
    "incremental_conditions" : {
      "param_chem_pot" : {
        "a" : 0.0
      },
      "temperature" : 10.0,
      "tolerance" : 0.001
    }
  }
}
-------

EXAMPLE: Settings for an custom drive mode LTE1 calculation with
increasing temperature.
-------
{
  "comment" : "This is a sample input file. Unrecognized attributes (like the ones prepended with '_' are ignored.",
  "debug" : false,
  "ensemble" : "grand_canonical",
  "method" : "lte1",
  "model" : {
    "formation_energy" : "formation_energy"
  },
  "supercell" : [
    [9, 0, 0],
    [0, 9, 0],
    [0, 0, 9]
  ],
  "data" : {
    "storage" : {
      "write_observations" : false,
      "write_trajectory" : false,
      "output_format" : ["csv", "json"]
    }
  },
  "driver" : {
    "mode" : "incremental", 
    "motif" : {
      "configname" : "auto",
      "_configname" : "SCEL3_3_1_1_0_2_2/0",
      "_configdof" : "path/to/final_state.json"
    },
    "custom_conditions" : [
      {
        "param_chem_pot" : {
          "a" : 0.0
        },
        "temperature" : 100.0,
        "tolerance" : 0.001
      },
      {
        "param_chem_pot" : {
          "a" : 0.0
        },
        "temperature" : 200.0,
        "tolerance" : 0.001
      },
      {
        "param_chem_pot" : {
          "a" : 0.0
        },
        "temperature" : 400.0,
        "tolerance" : 0.001
      },
      {
        "param_chem_pot" : {
          "a" : 0.0
        },
        "temperature" : 800.0,
        "tolerance" : 0.001
      }
    ]
  }
}
-------
```
</details>
<br>
