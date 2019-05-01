A common approach is to first enumerate symmetrically unique supercells and then enumerate configurations within a supercell.

A supercell can be represented by a transformation matrix, `T`:

  `S = P * T `,

where `S` is a 3x3 column vector matrix containing the supercell lattice vectors, and `P` is a 3x3 column vector matrix containting the primitive cell lattice vectors.

|![scel_transf_mat]({{ site.baseurl }}/assets/tutorials/enum/scel_enum.0.png){:width="650px"}|
|The supercell transformation matrix.|

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
