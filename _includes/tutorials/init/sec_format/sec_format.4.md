For a description of how to include template Quantum Espresso input files and set options that control the calculation method, use `` `casm format --qe` ``:"

```
$ casm format --qe
```
<details><summary markdown="span">See result</summary>

```
$ casm format --qe

### quantum espresso ##################

LOCATION WHEN GENERATED:

INPUT SETTINGS:
$CALC_SETTINGS/relax.json
$CALC_SETTINGS/$CUSTOM_INFILE_NAME
$CALC_SETTINGS/SPECIES
For global settings:
  CALC_SETTINGS = $ROOT/training_data/settings/$CURR_CALCTYPE
For supercell specific settings:
  CALC_SETTINGS = $ROOT/training_data/$SCELNAME/settings/$CURR_CALCTYPE
For configuration specific settings:
  CALC_SETTINGS = $ROOT/training_data/$SCELNAME/$CONFIGID/settings/$CURR_CALCTYPE

RESULTS:
$ROOT/training_data/$SCELNAME/$CONFIGID/$CURR_CALCTYPE/(quantum espresso results)
$ROOT/training_data/$SCELNAME/$CONFIGID/$CURR_CALCTYPE/properties.calc.json (read)


DESCRIPTION:
CASM comes with wrappers for using Quantum Espresso to calculate the properties 
of configurations, but is designed so that any type of calculation  
software or method could be used if an appropriate set of wrapper   
scripts are available. By convention, input settings for software   
used to calculate the properties of a particular configuration      
should be checked for in the following directories:                 
  1) $ROOT/training_data/$SCELNAME/$CONFIGID/settings/$CURR_CALCTYPE
  2) $ROOT/training_data/$SCELNAME/settings/$CURR_CALCTYPE          
  3) $ROOT/training_data/settings/$CURR_CALCTYPE                    

The Quantum Espresso wrappers included with CASM check for input settings files 
in the above directories, using the most local settings for a       
particular configuration. In most cases, the global settings files  
are stored in $ROOT/training_data/settings/$CURR_CALCTYPE and used  
for all configurations. Settings files are searched for on a file-by-file
basis, so to set supercell or configuration specific settings it is 
sufficient to only include the particular files necessary in the    
supercell or configuration level settings folder.                   

PBS job submission using the Quantum Espresso wrappers depends on using the pbs 
python module available here: https://github.com/prisms-center/pbs  

Included with CASM, the 'qe.relax' script can be executed by the  
'casm run' command to submit a batch of Quantum Espresso jobs that for selected 
configurations. For each selected configuration, Quantum Espresso is re-run
using the output of the previous calculation until full convergence 
is achieved. The convergence criteria is: if the cell shape and     
volume remain constant (calculation != vc-relax) then a single calculation  
is performed; else the calculation is converged if at least 2 jobs  
are complete, and: 1) the last job completed with <= 3 ionic steps  
 or, if "nrg_convergence" is set in the 'relax.json' file, 2) the 
last two calculations had final energy differ by less than the value of 
 "nrg_convergence". Once converged, a final constant volume       
calculation is performed with the following setting: (calculation = 'relax')
relax.json:                                                         
  This JSON file contains a single JSON object which contains       
  parameters used to control PBS job submission settings.           
  Required keys are:                                                
    "queue": queue to submit job in                               
    "ppn": processors (cores) per node to request                 
    "atom_per_proc": max number of atoms per processor (core)     
    "walltime": walltime to request (ex. "48:00:00")            

    "software": needs to be quantumespresso for quantum espresso to be used

 Optional keys are:                                                 
    "account": account to submit job under (default None)         
    "pmem": string for requested memory (default None)            
    "priority": requested job priority (default "0")            
    "message": when to send messages about jobs (ex. "abe",     
               default "a")                                       
    "email": where to send messages (ex. "me@fake.com", default 
             None)                                                  
    "qos": quality of service, 'qos' option (ex. "fluxoe")      
    "qe_cmd": quantum espresso execution command (default is "pw.x < {INFILE} > {OUTFILE}" if    
                ncpus=1, else "mpirun -np {NCPUS} pw.x < {INFILE} > {OUTFILE}"           
    "infile": quantum espresso input file name (default is "std.in"
    "outfile": quantum espresso output file name (default is "std.out"
    "ncpus": number of cpus (cores) to run on (default $PBS_NP)   
    "run_limit": number of vasp runs until "not_converging"     
                 (default 10)                                       
    "nrg_convergence": converged if last two runs complete and    
                       differ in energy by less than this amount    
                       (default None)                               
    "move": files to move at the end of a run (ex. "",    
            ".wfc"], default [])                     
    "copy": files to copy from run to run  default [$infilename]) 
    "remove": files to remove at the end of a run                
               default [".wfc", ".igk", ".save"]             
    "compress": files to compress at the end of a run (ex.        
                [$outfilename], default [])          
    "backup": files to compress to backups at the end of a run,   
              used in conjunction with move (ex. [".wfc"])     
    "extra_input_files": extra input files to be copied from the  
                         settings directory, e.g., an OCCUPATIONS     
                         file.                                      
    "initial": location of $infile with tags for the initial run,   
               if desired                                            
    "final": location of $infile with tags for the final run, if  
             desired                                                
    "err_types": list of errors to check for. Not Implemented yet  

EXAMPLE: relax.json 
-------
{
  "account":"prismsprojectdebug_flux",
  "queue":"flux",
  "priority":"-200",
  "walltime":"1:00:00",
  "pmem":"3800mb",
  "email":"username@univ.edu",
  "ppn":"16",
  "atom_per_proc":"2",
  "run_limit":10,
  "nrg_convergence":0.002
  "calculator":"quantumespresso"
  "infilename":"LixCoO2.in"
  "outfilename":"LixCoO2.out"
}
-------


SPECIES:                                                            
  This file contains information for selecting pseudopotentials and specifing
  parameters that must be set on an atom-by-atom basis in the infile,
  such as magnetic moment (non currently implemented).
  The first line in the file specifies the value of 
  'PSEUDO_DIR_PATH', which is the base path used to find UPF     
  files. The second line contains column headings (at least 4), and 
  then there are lines for each distinct species. The first column  
  specifies the 'SPECIES' and must match a species names in the PRIM
  file. The second column gives an 'ALIAS' name for the species which
  is used for ordering like atoms in the generated input files. The
  third column should be either '0' or '1', such that only one      
  species with a given ALIAS has a '1'. For that species the fourth 
  column must contain the path that should be appended to the       
  PSEUDO_DIR_PATH to specify the UPF file for that species.      

  Additional columns, such as 'if_pos' in the example below are     

  and used to specify the value used for a particular species in the
  infile. The column heading must match a valid quantum espresso input setting.
  For now only supported additional tag is if_pos, a way to fixed certain lattice positions.

EXAMPLE: SPECIES 
-------
PSEUDO_DIR_PATH = /absolute/path/to/quantumespresso_potentials
SPECIES    ALIAS    UPF  UPF_location     if_pos
Ni         Ni       1       PAW_PBE/Ni.UPF     1,1,1
Al        Al       1       PAW_PBE/Al.UPF      1,1,1
-------


$infilename:                                                              
  This is a template input file used for Quantum Espresso calculations. The settings 
  are generally used as given though some may be automatically set  
  based on settings in the 'relax.json' or 'SPECIES' files. Also,   
  some settings might be added or changed if certain errors are     
  during calculation. The actual input file used for each calculation is 
  saved.                                                            

Note:                                                    
  K_POINTS will be adjusted accordingly such that the density is maintained
  over all configurations in the project for all Quantum Espresso calculations
  this uses the CELL_PARAMETERS and the K_POINTS cards in the input file to calculate
  a density and rescale configurations k-point mesh accordingly
EXAMPLE: Mg2Ti4S8.in 
-------
System = Test of Quantum Espresso submission
&CONTROL
 calculation = 'vc-relax',
 pseudo_dir = '/home/skolli/quantum_espresso/pseudo/',
 tprnfor = .true.,
 prefix = 'Mg2Ti4S8',
 restart_mode = 'from_scratch',
 tstress = .true.,
/
&SYSTEM
 ecutwfc = 45.0,
 occupations = 'fixed',
 celldm(1) = 7.3794,
 ibrav = 0,
 nat = 14,
 ntyp = 3,
 ecutrho = 200.0,
/
&ELECTRONS
 diagonalization = 'cg',
 mixing_mode = 'plain',
 mixing_beta = 0.7,
 conv_thr = 1e-08,
/
&IONS
 ion_dynamics = 'bfgs',
/
&CELL
 press = 0.1,
 cell_factor = 1.6,
 cell_dynamics = 'bfgs',
/

ATOMIC_SPECIES
 Mg 24.31 Mg.pbe-nsp-bpaw.UPF
 Ti 47.88 Ti.pbe-sp-hgh.UPF
 S 32.07 S.pbe-n-kjpaw_psl.0.1.UPF

CELL_PARAMETERS angstrom
 0.0000000000000000 5.1756022947592379 5.1756022947592388
 5.1756022947592388 0.0000000000000000 5.1756022947592388
 5.1756022947592388 5.1756022947592379 0.0000000000000000

ATOMIC_POSITIONS crystal
Mg 0.000000000 0.000000000 0.000000000
Mg 0.250000000 0.250000000 0.250000000
Ti 0.625000000 0.625000000 0.625000000
Ti 0.125000000 0.625000000 0.625000000
Ti 0.625000000 0.125000000 0.625000000
Ti 0.625000000 0.625000000 0.125000000
S 0.3842989149764762 0.3842989149764762 0.3842989149764762
S 0.8657010850235238 0.8657010850235238 0.8657010850235238
S 0.3842989149764762 0.8471032550705786 0.3842989149764762
S 0.3842989149764762 0.3842989149764762 0.8471032550705786
S 0.8471032550705786 0.3842989149764762 0.3842989149764762
S 0.8657010850235238 0.8657010850235238 0.4028967449294214
S 0.8657010850235238 0.4028967449294214 0.8657010850235238
S 0.4028967449294214 0.8657010850235238 0.8657010850235238

K_POINTS automatic
 6 6 6 0 0 0

-------
```
</details>
<br>
