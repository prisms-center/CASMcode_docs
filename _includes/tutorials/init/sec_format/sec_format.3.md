Python wrappers allow CASM to interact with VASP, Quantum Espresso, and other first-principles software to setup input files, run calculations interactively or sumbit jobs on a cluster, handle errors, and parse output files.

For a description of how to include template VASP input files and set options that control the calculation method, use `` `casm format --vasp` ``:"

```
$ casm format --vasp
```
<details><summary markdown="span">See result</summary>

```
$ casm format --vasp

### vasp ##################

LOCATION WHEN GENERATED:

INPUT SETTINGS:
$CALC_SETTINGS/relax.json
$CALC_SETTINGS/INCAR
$CALC_SETTINGS/SPECIES
$CALC_SETTINGS/KPOINTS
$CALC_SETTINGS/POSCAR

For global settings:
  CALC_SETTINGS = $ROOT/training_data/settings/$CURR_CALCTYPE
For supercell specific settings:
  CALC_SETTINGS = $ROOT/training_data/$SCELNAME/settings/$CURR_CALCTYPE
For configuration specific settings:
  CALC_SETTINGS = $ROOT/training_data/$SCELNAME/$CONFIGID/settings/$CURR_CALCTYPE

RESULTS:
$ROOT/training_data/$SCELNAME/$CONFIGID/$CURR_CALCTYPE/(VASP results)
$ROOT/training_data/$SCELNAME/$CONFIGID/$CURR_CALCTYPE/properties.calc.json (read)


DESCRIPTION:
CASM comes with wrappers for using VASP to calculate the properties 
of configurations, but is designed so that any type of calculation  
software or method could be used if an appropriate set of wrapper   
scripts are available. By convention, input settings for software   
used to calculate the properties of a particular configuration      
should be checked for in the following directories:                 
  1) $ROOT/training_data/$SCELNAME/$CONFIGID/settings/$CURR_CALCTYPE
  2) $ROOT/training_data/$SCELNAME/settings/$CURR_CALCTYPE          
  3) $ROOT/training_data/settings/$CURR_CALCTYPE                    

The VASP wrappers included with CASM check for input settings files 
in the above directories, using the most local settings for a       
particular configuration. In most cases, the global settings files  
are stored in $ROOT/training_data/settings/$CURR_CALCTYPE and used  
for all configurations. Settings files are searched for on a file-by-file
basis, so to set supercell or configuration specific settings it is 
sufficient to only include the particular files necessary in the    
supercell or configuration level settings folder.                   

PBS job submission using the VASP wrappers depends on using the pbs 
python module available here: https://github.com/prisms-center/pbs  

Included with CASM, the 'vasp.relax' script can be executed by the  
'casm run' command to submit a batch of VASP jobs that for selected 
configurations. For each selected configuration, VASP is re-run     
using the output of the previous calculation until full convergence 
is achieved. The convergence criteria is: if the cell shape and     
volume remain constant (ISIF=0, 1, or 2) then a single calculation  
is performed; else the calculation is converged if at least 2 jobs  
are complete, and: 1) the last job completed with <= 3 ionic steps  
 or, if "nrg_convergence" is set in the 'relax.json' file, 2) the 
last two calculations had final E0 differ by less than the value of 
 "nrg_convergence". Once converged, a final constant volume       
calculation is performed with the following INCAR settings: (ISIF=2,
ISMEAR=-5, NSW=0, IBRION=-1).                                       

relax.json:                                                         
  This JSON file contains a single JSON object which contains       
  parameters used to control PBS job submission settings.           
  Required keys are:                                                
    "queue": queue to submit job in                               
    "ppn": processors (cores) per node to request                 
    "atom_per_proc": max number of atoms per processor (core)     
    "walltime": walltime to request (ex. "48:00:00")            

 Optional keys are:                                                 
    "account": account to submit job under (default None)         
    "pmem": string for requested memory (default None)            
    "priority": requested job priority (default "0")            
    "message": when to send messages about jobs (ex. "abe",     
               default "a")                                       
    "email": where to send messages (ex. "me@fake.com", default 
             None)                                                  
    "qos": quality of service, 'qos' option (ex. "fluxoe")      
    "npar": vasp incar setting (default None)                     
    "ncore": vasp incar setting (default None)                    
    "kpar": vasp incar setting (default None)                     
    "vasp_cmd": vasp execution command (default is "vasp" if    
                ncpus=1, else "mpirun -np {NCPUS} vasp"           
    "ncpus": number of cpus (cores) to run on (default $PBS_NP)   
    "run_limit": number of vasp runs until "not_converging"     
                 (default 10)                                       
    "nrg_convergence": converged if last two runs complete and    
                       differ in energy by less than this amount    
                       (default None)                               
    "move": files to move at the end of a run (ex. "POTCAR",    
            "WAVECAR"], default ["POTCAR"])                     
    "copy": files to copy from run to run (ex. ["INCAR",        
            "KPOINTS"], default ["INCAR, KPOINTS"])             
    "remove": files to remove at the end of a run (ex. ["IBZKPT",
              "CHGCAR"], default ["IBKZPT", "CHG", "CHGCAR",
              "WAVECAR", "TMPCAR", "EIGENVAL", "DOSCAR",    
              "PROCAR", "PCDAT", "XDATCAR", "LOCPOT", "ELFCAR",
              "PROOUT"]                                           
    "compress": files to compress at the end of a run (ex.        
                ["OUTCAR", "vasprun.xml"], default [])          
    "backup": files to compress to backups at the end of a run,   
              used in conjunction with move (ex. ["WAVECAR"])     
    "encut": [START, STOP, STEP] values for converging ENCUT to   
             within nrg_convergence (ex. ["450", "Auto",        
             "10"], default ["Auto", "Auto", "10"] where    
             "Auto" is either the largest ENMAX in all POTCARS    
             called in SPECIES for START, or 2.0 * largest ENMAX    
             for STOP)                                              
    "kpoints": [start, stop, step] values for converging KPOINTS  
               to within nrg_convergence (ex. ["5", "50", "1"],
               default ["5", "Auto", "1"] where "Auto" can  
               only be used for STOP and means to keep increasing   
               the KPOINTS length by STEP until either              
               nrg_convergence or walltime is reached). For meaning 
               of the KPOINTS length parameter see the VASP         
               documentation at http://cms.mpi.univie.ac.at/vasp/   
               vasp/Automatic_k_mesh_generation.html                
    "extra_input_files": extra input files to be copied from the  
                         settings directory, e.g., a vdW kernel     
                         file.                                      
    "initial": location of INCAR with tags for the initial run,   
               if desired (e.g. to generate a PBE WAVECAR for use   
               with M06-L)                                          
    "final": location of INCAR with tags for the final run, if    
             desired (e.g. "ISMEAR = -5", etc). Otherwise, the    
             settings enforced are ("ISMEAR = -5", "NSW = 0",   
              "IBRION = -1", "ISIF = 2")                        
    "err_types": list of errors to check for. Allowed entries are 
                 "IbzkptError" and "SubSpaceMatrixError".       
                 Default: ["SubSpaceMatrixError"]                 

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
}
-------


SPECIES:                                                            
  This file contains information for selecting POTCARs and specifing
  parameters that must be set on an atom-by-atom basis in the INCAR,
  such as MAGMOM. The first line in the file specifies the value of 
  'POTCAR_DIR_PATH', which is the base path used to find POTCAR     
  files. The second line contains column headings (at least 4), and 
  then there are lines for each distinct species. The first column  
  specifies the 'SPECIES' and must match a species names in the PRIM
  file. The second column gives an 'ALIAS' name for the species which
  is used for ordering like atoms in the generated POSCAR files. The
  third column should be either '0' or '1', such that only one      
  species with a given ALIAS has a '1'. For that species the fourth 
  column must contain the path that should be appended to the       
  POTCAR_DIR_PATH to specify the POTCAR file for that species.      

  Additional columns, such as 'MAGMOM' in the example below are     

  and used to specify the value used for a particular species in the
  INCAR. The column heading must match a valid VASP INCAR setting.  

EXAMPLE: SPECIES 
-------
POTCAR_DIR_PATH = /absolute/path/to/vasp_potentials
SPECIES    ALIAS    POTCAR  POTCAR_location    MAGMOM
Mn3        Mn       0       -                  3
Mn4        Mn       1       PAW_PBE/Mn         4
-------


INCAR:                                                              
  This is a template INCAR used for VASP calculations. The settings 
  are generally used as given though some may be automatically set  
  based on settings in the 'relax.json' or 'SPECIES' files. Also,   
  some settings might be added or changed if certain errors are     
  during calculation. The actual INCAR used for each calculation is 
  saved.                                                            

EXAMPLE: INCAR 
-------
System = Test of VASP submission
ISPIN = 1 # non-spin polarized
PREC = Accurate 
IBRION = 2 # conjugate gradient ionic minimization
NSW = 61
ISIF= 3 # relax ions and volume
ENMAX = 400 
ISMEAR = 1 # for metals
SIGMA = 0.2 
LWAVE = .FALSE.
LCHARG = .FALSE.
-------


KPOINTS, POSCAR:                                                    
  This is a template KPOINTS file used for VASP calculations. If the
  mode (third line) is set to 'Auto', this file is used as is for all
  VASP calculations.  Otherwise, if the mode is 'Gamma' or 'M', a   
  reference POSCAR must also exist and a scaling method is used to  
  calculate the kpoint mesh for a supercell, such that it has an    
  equal or greater kpoint density than in the reference POSCAR.     

-------
```
</details>
<br>
