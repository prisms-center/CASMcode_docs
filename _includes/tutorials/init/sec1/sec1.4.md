The `` `casm status` `` command is very useful for getting information about the current status of a project. The `` `-n` `` option also gives suggestions for the next steps that you might take for the workflow of a typical CASM project. At this point, the command just indicates that no project has been initialized.
```
$ casm status -n
```
<details><summary markdown="span">See result</summary>

```
$ casm status -n

~~~ Error loading casm libraries ~~~
find_executable('ccasm'): None
Could not find 'ccasm' executable. CASM is not installed on your PATH.
Install CASM if it is not installed, or update your PATH, or set LIBCASM to the location of libcasm.

Could not find libcasm. Please check your installation.
```
</details>
<br>
