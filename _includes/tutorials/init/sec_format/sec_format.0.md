The `` `casm format` `` command provides a description of CASM input files and the CASM project directory structure. For a list of all options, use `` `casm format -h` ``:

```
$ casm format -h
```
<details><summary markdown="span">See result</summary>

```
$ casm format -h

'casm format' usage:
  -h [ --help ]         Print help message
  --desc                Print extended usage description
  -d [ --dir ]          CASM project directory structure summary
  --project_settings    Description and location of 'project_settings' file
  --prim                Description and location of 'prim.json' and 'PRIM' 
                        files
  --config_list         Description and location of 'config_list.json' file
  --sym                 Description and location of 'lattice_point_group.json',
                        'factor_group.json' and 'crystal_point_group.json' 
                        files
  --vasp                Description and location of VASP settings files
  --properties          Description and location of properties.calc.json files
  --qe                  Description and location of Quantum Espresso settings 
                        files
  --comp                Description and location of 'composition_axes.json' 
                        file
  --bspecs              Description and location of 'bspecs.json' file
  --clust               Description and location of 'clust.json' file
  --basis               Description and location of 'basis.json' file
  --clex                Description and location of '$TITLE_Clexulator.*' files
  --ref                 Description and location of 'chemical_reference.json' 
                        files
  --scel                Description and location of 'SCEL' file
  --lat                 Description and location of 'LAT' files
  --pos                 Description and location of 'POS' files
  --eci                 Description and location of 'eci.json' file
  --monte               Description and location of the Monte Carlo input file
```
</details>
<br>
