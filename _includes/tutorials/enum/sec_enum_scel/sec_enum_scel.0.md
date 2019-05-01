In CASM, crystal states consistent with the primitive crystal structure are called "configurations". Each configuration can be represented by specifying:

- supercell vectors used to repeat a unit cell into the infinite crystal
- the value of local degrees of freedom at each site in the unit cell, including:
  - discrete site DoF (atom or molecule site occupant)
  - continuous site DoF (ex: displacement vector)
- the value of global degrees of freedom (ex: strain)

Each CASM project contains a database of enumerated supercells and configurations, which may have been generated in a variety of different ways. The primary approach is to enumerate them directly using methods accessed via the `` `casm enum` `` subcommand.

From within a CASM project, the list of enumeration methods can be printed using `` `casm enum -h` ``.

```
$ casm enum -h
```
<details><summary markdown="span">See result</summary>

```
$ casm enum -h
-- Construct: CASM Project -- 
from: "/Users/bpuchala/mcproj/CASM_test_projects/0.3.X/ZrO_tutorial"

-- Load project data -- 
read: "/Users/bpuchala/mcproj/CASM_test_projects/0.3.X/ZrO_tutorial/.casm/composition_axes.json"


'casm enum' usage:
  -h [ --help ]                 Print help message.
  --desc arg                    Print extended usage description. Use '--desc 
                                MethodName [MethodName2...]' for detailed 
                                option description. Partial matches of method 
                                names will be included.
  -m [ --method ] arg           Method to use: Can use number shortcuts in this
                                option.
  --min arg (=1)                Min volume
  --max arg                     Max volume
  --filter <query>              Filter configuration enumeration so that only 
                                configurations matching a 'casm query'-type 
                                expression are recorded
  -a [ --all ]                  Enumerate configurations for all existing 
                                supercells
  --verbosity arg (=standard)   Verbosity of output. Options are 'none', 
                                'quiet', 'standard', 'verbose', 'debug', or an 
                                integer 0-100 (0: none, 100: all).
  -s [ --settings ] <path>      Settings input file specifying which parameters
                                should be used. See 'casm format --enum'.
  -i [ --input ] arg            String specifying input settings. See 'casm 
                                format --enum'.
  --scelnames <supercell>       One or more supercells to use casm enum with, 
                                such as 'SCEL4_2_2_1_0_0_0'
  --confignames <configuration> One or more configurations to use casm enum 
                                with, such as 'SCEL4_2_2_1_0_0_0/3'

The enumeration methods are:

  0) ConfigEnumAllOccupations
  1) ConfigEnumRandomOccupations
  2) ScelEnum
  3) SuperConfigEnum

For complete options description, use 'casm enum --desc MethodName'.
```
</details>
<br>
