{% include tutorials/init/sec3/sec3.0-desc.md %}
```
$ ls -h -l -a .
$ casm init
```
<details><summary markdown="span">See result</summary>

```
$ ls -h -l -a .
total 16
drwxr-xr-x  9 bpuchala  staff   288B Aug  4 22:58 .
drwxr-xr-x  5 bpuchala  staff   160B Aug  4 22:58 ..
drwxr-xr-x  4 bpuchala  staff   128B Aug  4 22:59 .casm
-rw-r--r--  1 bpuchala  staff   1.1K Aug  4 22:59 LOG
drwxr-xr-x  3 bpuchala  staff    96B Aug  4 22:58 basis_sets
drwxr-xr-x  3 bpuchala  staff    96B Aug  4 22:58 cluster_expansions
-rw-r--r--  1 bpuchala  staff   815B Aug  7 08:55 prim.json
drwxr-xr-x  5 bpuchala  staff   160B Aug  4 22:58 symmetry
drwxr-xr-x  3 bpuchala  staff    96B Aug  4 22:58 training_data
$ casm init

~~~ Error loading casm libraries ~~~
find_executable('ccasm'): None
Could not find 'ccasm' executable. CASM is not installed on your PATH.
Install CASM if it is not installed, or update your PATH, or set LIBCASM to the location of libcasm.

Could not find libcasm. Please check your installation.
```
</details>
<br>
