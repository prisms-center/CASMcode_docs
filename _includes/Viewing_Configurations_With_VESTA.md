### Configuration and use of `casm view`

The `casm view` command is a shortcut for viewing CASM configurations in visualization software, such as VESTA. 

It writes POSCAR files for one or more configurations and runs a subcommand to launch a visualization program that can view those files.

Often it is used with [VESTA](https://jp-minerals.org/vesta/) though it could be configured to work with other software.

### Example usage

- Note proper configuration depends on having VESTA installed and accessible as this example configures it. It may need to be customized for your system

This example will:

1. Create an example project
2. Enumerate configurations in that project
3. Configure `casm view` to launch VESTA
4. View a configuration in VESTA
5. View multiple configurations in VESTA at once


```python
import os
import pathlib
import tempfile
tutorials_dir = os.getcwd()

# use a temporary directory for the CASM project 
# - change this to where you want to create a project
project_tmpdir = tempfile.TemporaryDirectory()
project_path = pathlib.Path(project_tmpdir.name)

# copy the ZrO prim file to the new project directory
!cp $tutorials_dir/primfiles/ZrO_prim.json $project_path/prim.json

# change the current working directory to the new project directory
%cd $project_path

# initialize the project & set default composition axes
!ccasm init
!ccasm composition --calc && ccasm composition --select 0

# enumerate configurations up to supercell size 4
!ccasm enum -m ConfigEnumAllOccupations --max 4
```

    /private/var/folders/v7/lq3_7hgj7n95d1xrct505ryh0000gp/T/tmpk6cgazo_
    
    ***************************
    
    Initializing CASM project 'ZrO'
    Creating CASM project directory tree at: "/private/var/folders/v7/lq3_7hgj7n95d1xrct505ryh0000gp/T/tmpk6cgazo_"
    Writing prim file: "/private/var/folders/v7/lq3_7hgj7n95d1xrct505ryh0000gp/T/tmpk6cgazo_/.casm/prim.json"
      DONE
    
    
    ***************************
    
    Using the PRIM to enumerate standard composition axes for this space.
    
    Possible composition axes:
    
           KEY     ORIGIN          a     GENERAL FORMULA
           ---        ---        ---     ---
             0  Zr(2)O(2) Zr(2)Va(2)     Zr(2)Va(2a)O(2-2a)
             1 Zr(2)Va(2)  Zr(2)O(2)     Zr(2)Va(2-2a)O(2a)
    
    
    
    Wrote: "/private/var/folders/v7/lq3_7hgj7n95d1xrct505ryh0000gp/T/tmpk6cgazo_/.casm/composition_axes.json"
    
    Please use 'casm composition --select' to choose your composition axes.
    
    
    ***************************
    
    Possible composition axes:
    
           KEY     ORIGIN          a     GENERAL FORMULA
           ---        ---        ---     ---
             0  Zr(2)O(2) Zr(2)Va(2)     Zr(2)Va(2a)O(2-2a)
             1 Zr(2)Va(2)  Zr(2)O(2)     Zr(2)Va(2-2a)O(2a)
    
    Currently selected composition axes: 0
    
    Parametric composition:
      comp(a) = 0.25*comp_n(Va)  - 0.25*(comp_n(O) - 2) 
    
    Composition:
      comp_n(Zr) = 2
      comp_n(Va) = 2*comp(a) 
      comp_n(O) = 2 - 2*comp(a) 
    
    Parametric chemical potentials:
      param_chem_pot(a) = -2*chem_pot(O) 
    
    
    Wrote: "/private/var/folders/v7/lq3_7hgj7n95d1xrct505ryh0000gp/T/tmpk6cgazo_/.casm/composition_axes.json"
    
    -- Begin: ConfigEnumAllOccupations -- 
    Input from JSON (--input or --setings):
    {
    }
    
    Input from `casm enum` options:
    {
      "max" : 4,
      "method" : "ConfigEnumAllOccupations"
    }
    
    Combined Input:
    {
      "supercells" : {
        "max" : 4
      }
    }
    
    -- Checking input -- 
    primitive_only: true
    filter: false
    verbosity: 10
    dry_run: false
    output_configurations: false
    # of initial enumeration states: 20
    
    -- Begin: ConfigEnumAllOccupations enumeration -- 
    # configurations in this project: 0
    Begin enumeration
    
    Enumerate configurations for: SCEL1_1_1_1_0_0_0
    3 configurations (3 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL2_1_2_1_0_0_0
    4 configurations (4 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL2_1_2_1_1_0_0
    3 configurations (3 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL2_1_1_2_0_0_0
    3 configurations (3 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL3_3_1_1_0_0_1
    10 configurations (10 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL3_3_1_1_0_0_2
    10 configurations (10 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL3_1_3_1_2_0_0
    16 configurations (16 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL3_3_1_1_0_2_2
    10 configurations (10 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL3_1_1_3_0_0_0
    10 configurations (10 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_1_4_1_0_0_0
    27 configurations (27 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_2_2_1_0_0_1
    27 configurations (27 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_1_4_1_1_0_0
    42 configurations (42 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_4_1_1_0_3_2
    24 configurations (24 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_1_4_1_2_0_0
    24 configurations (24 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_2_2_1_0_1_1
    21 configurations (21 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_2_2_1_0_0_0
    15 configurations (15 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_2_2_1_0_1_0
    18 configurations (18 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_1_2_2_0_0_0
    21 configurations (21 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_1_2_2_1_0_0
    24 configurations (24 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_1_1_4_0_0_0
    24 configurations (24 new, 0 excluded by filter).
    
    Enumeration complete
    
    # new configurations: 336
    # configurations in this project: 336
    
    Write supercell database... DONE
    Write configuration database... DONE


### Create a selection at a particular composition


```python
# view a list of configurations at composition ZrO_{1/6}
atom_frac_O = 1./(6.+1.)
atom_frac_O_plus = atom_frac_O + 0.01
atom_frac_O_minus = atom_frac_O - 0.01
!ccasm select --set 'lt(atom_frac(O),'$atom_frac_O_plus')' 
!ccasm select --set-off 'lt(atom_frac(O),'$atom_frac_O_minus')'
!ccasm query -k 'atom_frac(O)' -o STDOUT
```

    -- Input config list: MASTER -- 
    # configs in this project: 336
    # configs included in this list: 336
    # configs selected in this list: 0
    
    -- set: lt(atom_frac(O),0.15285714285714286) -- 
    selection time: 0.0014823 (s)
    
    -- Write: Selection -- 
    write: "MASTER"
    
    -- Output config list: MASTER -- 
    # configs in this project: 336
    # configs included in this list: 336
    # configs selected in this list: 19
    
    -- Input config list: MASTER -- 
    # configs in this project: 336
    # configs included in this list: 336
    # configs selected in this list: 19
    
    -- set-off: lt(atom_frac(O),0.13285714285714284) -- 
    selection time: 0.000152694 (s)
    
    -- Write: Selection -- 
    write: "MASTER"
    
    -- Output config list: MASTER -- 
    # configs in this project: 336
    # configs included in this list: 336
    # configs selected in this list: 6
    
    Print:
       - atom_frac(O)
    to "STDOUT"
    
    #                  name    selected    atom_frac(O)
        SCEL3_1_1_3_0_0_0/0           1      0.14285714
        SCEL3_1_3_1_2_0_0/0           1      0.14285714
        SCEL3_1_3_1_2_0_0/2           1      0.14285714
        SCEL3_3_1_1_0_0_1/0           1      0.14285714
        SCEL3_3_1_1_0_0_2/0           1      0.14285714
        SCEL3_3_1_1_0_2_2/0           1      0.14285714
    
       -Output printed to terminal, since no output file specified-
      DONE.
    


<div class="alert alert-warning">
<b>Reminder:</b> 
    
This is an example configuration of `casm view` to use VESTA.

- It requires VESTA to be installed
- The correct configuration on your local machine depends on your VESTA installation
- For use on linux, try adjusting the comments to try the linux configuration.
- To check if the configuration is successful, try the following cells
</div>


```python
# example osx config: 
!ccasm settings --set-view-command \
   'casm.view "open -a /Applications/VESTA/VESTA.app"'

# example linux config: 
#   casm settings --set-view-command ’casm.view VESTA’
```

    Set view command to: 'casm.view "open -a /Applications/VESTA/VESTA.app"'
    



```python
# This might an interesting configuration to view...
!ccasm view --confignames SCEL3_3_1_1_0_2_2/0

# Note: If the configuration is correct, 
# 1 POSCAR will be printed and opened in VESTA
```

    SCEL3_3_1_1_0_2_2/0:
    casm.view "open -a /Applications/VESTA/VESTA.app" /private/var/folders/v7/lq3_7hgj7n95d1xrct505ryh0000gp/T/tmpk6cgazo_/.casm/tmp/POSCAR 2>&1
    Begin casm.view
    Reading POSCAR:
    
    1.00000000
    4.85098029 2.80071477 0.00000000
    0.00000000 5.60142954 0.00000000
    1.61699343 2.80071477 5.16867834
    O Zr 
    1 6 
    Direct
    -0.08333333 0.25000000 0.25000000 O
    0.00000000 0.00000000 0.00000000 Zr
    0.66666667 0.66666667 0.00000000 Zr
    0.33333333 0.33333333 0.00000000 Zr
    0.16666667 -0.16666667 0.50000000 Zr
    0.83333333 0.50000000 0.50000000 Zr
    0.50000000 0.16666667 0.50000000 Zr
    
    



```python
# open all selected configurations
!ccasm view --config MASTER

# Note: If the configuration is correct, 
# 6 POSCARs will be printed and opened in VESTA
```

    SCEL3_1_1_3_0_0_0/0:
    casm.view "open -a /Applications/VESTA/VESTA.app" /private/var/folders/v7/lq3_7hgj7n95d1xrct505ryh0000gp/T/tmpk6cgazo_/.casm/tmp/POSCAR 2>&1
    Begin casm.view
    Reading POSCAR:
    
    1.00000000
    3.23398686 0.00000000 0.00000000
    -1.61699343 2.80071477 0.00000000
    0.00000000 0.00000000 15.50603502
    O Zr 
    1 6 
    Direct
    0.33333333 0.66666667 0.08333333 O
    0.00000000 0.00000000 0.00000000 Zr
    0.00000000 0.00000000 0.33333333 Zr
    0.00000000 0.00000000 0.66666667 Zr
    0.66666667 0.33333333 0.16666667 Zr
    0.66666667 0.33333333 0.50000000 Zr
    0.66666667 0.33333333 0.83333333 Zr
    
    
    SCEL3_1_3_1_2_0_0/0:
    casm.view "open -a /Applications/VESTA/VESTA.app" /private/var/folders/v7/lq3_7hgj7n95d1xrct505ryh0000gp/T/tmpk6cgazo_/.casm/tmp/POSCAR 2>&1
    Begin casm.view
    Reading POSCAR:
    
    1.00000000
    3.23398686 0.00000000 0.00000000
    -1.61699343 2.80071477 -5.16867834
    0.00000000 5.60142954 5.16867834
    O Zr 
    1 6 
    Direct
    0.02777778 0.05555556 0.30555556 O
    0.00000000 0.00000000 0.00000000 Zr
    0.33333333 0.66666667 0.66666667 Zr
    0.66666667 0.33333333 0.33333333 Zr
    0.38888889 -0.22222222 0.27777778 Zr
    0.72222222 0.44444444 0.94444444 Zr
    1.05555556 0.11111111 0.61111111 Zr
    
    
    SCEL3_1_3_1_2_0_0/2:
    casm.view "open -a /Applications/VESTA/VESTA.app" /private/var/folders/v7/lq3_7hgj7n95d1xrct505ryh0000gp/T/tmpk6cgazo_/.casm/tmp/POSCAR 2>&1
    Begin casm.view
    Reading POSCAR:
    
    1.00000000
    3.23398686 0.00000000 0.00000000
    -1.61699343 2.80071477 -5.16867834
    0.00000000 5.60142954 5.16867834
    O Zr 
    1 6 
    Direct
    -0.13888889 -0.27777778 0.47222222 O
    0.00000000 0.00000000 0.00000000 Zr
    0.33333333 0.66666667 0.66666667 Zr
    0.66666667 0.33333333 0.33333333 Zr
    0.38888889 -0.22222222 0.27777778 Zr
    0.72222222 0.44444444 0.94444444 Zr
    1.05555556 0.11111111 0.61111111 Zr
    
    
    SCEL3_3_1_1_0_0_1/0:
    casm.view "open -a /Applications/VESTA/VESTA.app" /private/var/folders/v7/lq3_7hgj7n95d1xrct505ryh0000gp/T/tmpk6cgazo_/.casm/tmp/POSCAR 2>&1
    Begin casm.view
    Reading POSCAR:
    
    1.00000000
    1.61699343 2.80071477 0.00000000
    0.00000000 0.00000000 5.16867834
    6.46797372 -5.60142954 0.00000000
    O Zr 
    1 6 
    Direct
    0.44444444 0.25000000 -0.11111111 O
    0.00000000 0.00000000 0.00000000 Zr
    0.33333333 0.00000000 0.66666667 Zr
    0.66666667 0.00000000 0.33333333 Zr
    0.55555556 0.50000000 0.11111111 Zr
    0.88888889 0.50000000 0.77777778 Zr
    1.22222222 0.50000000 0.44444444 Zr
    
    
    SCEL3_3_1_1_0_0_2/0:
    casm.view "open -a /Applications/VESTA/VESTA.app" /private/var/folders/v7/lq3_7hgj7n95d1xrct505ryh0000gp/T/tmpk6cgazo_/.casm/tmp/POSCAR 2>&1
    Begin casm.view
    Reading POSCAR:
    
    1.00000000
    0.00000000 0.00000000 5.16867834
    4.85098029 2.80071477 0.00000000
    -4.85098029 2.80071477 0.00000000
    O Zr 
    1 6 
    Direct
    0.25000000 0.33333333 0.33333333 O
    0.00000000 0.00000000 0.00000000 Zr
    0.00000000 0.66666667 0.33333333 Zr
    0.00000000 0.33333333 0.66666667 Zr
    0.50000000 0.33333333 -0.00000000 Zr
    0.50000000 1.00000000 0.33333333 Zr
    0.50000000 0.66666667 0.66666667 Zr
    
    
    SCEL3_3_1_1_0_2_2/0:
    casm.view "open -a /Applications/VESTA/VESTA.app" /private/var/folders/v7/lq3_7hgj7n95d1xrct505ryh0000gp/T/tmpk6cgazo_/.casm/tmp/POSCAR 2>&1
    Begin casm.view
    Reading POSCAR:
    
    1.00000000
    4.85098029 2.80071477 0.00000000
    0.00000000 5.60142954 0.00000000
    1.61699343 2.80071477 5.16867834
    O Zr 
    1 6 
    Direct
    -0.08333333 0.25000000 0.25000000 O
    0.00000000 0.00000000 0.00000000 Zr
    0.66666667 0.66666667 0.00000000 Zr
    0.33333333 0.33333333 0.00000000 Zr
    0.16666667 -0.16666667 0.50000000 Zr
    0.83333333 0.50000000 0.50000000 Zr
    0.50000000 0.16666667 0.50000000 Zr
    
    

