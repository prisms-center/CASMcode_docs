To get a list of `` `casm` `` subcommands, use `` `--desc` ``:
```
$ casm --desc
```
<details><summary markdown="span">See result</summary>

```
$ casm --desc
usage: casm [-h] [--desc] [--version] [--path PATH] [<command>] ...

CASM: First-principles based statistical mechanics

positional arguments:
  <command>    CASM command to execute
  ...          CASM command arguments

optional arguments:
  -h, --help   show this help message and exit
  --desc       Print command list
  --version    Print casm version
  --path PATH  Path to project. Default uses project containing current
               working directory.

available commands:
  bset
  calc
  composition
  enum
  exec
  files
  format
  help
  import
  init
  learn
  monte
  perturb
  plot
  query
  ref
  rm
  run
  select
  settings
  shell
  status
  super
  sym
  update
  version
  view

For help using a command: 'casm <command> --help'

For step by step help use: 'casm status -n'


```
</details>
<br>
