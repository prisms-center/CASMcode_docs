CASM generates a `` `LOG` `` file which records the steps performed while working on your project. The `` `LOG` `` file is not a 100% complete record. It is limited to logging particular subcommands and does not include other subcommands, such as `` `casm calc` `` or `` `casm learn` ``. Also, it does not record the values of input files at the time they were used. Despite being an incomplete record, it can still be a useful tool to remember actions taken in the CASM project.

```
$ grep casm LOG
```
<details><summary markdown="span">See result</summary>

```
$ grep casm LOG
casm sym -h 
casm sym 
casm sym --factor-group 
casm sym --lattice-point-group 
casm sym --crystal-point-group 
casm composition -d 
casm composition --select 0 
casm composition -d
```
</details>
<br>
