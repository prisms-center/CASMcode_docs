Use the `` `casm init` `` command in a directory with the `` `prim.json` `` file to intialize a new CASM project.

CASM defines a canonical form for structures to facilitate comparisons. The canonical form is:
- primitive
- with right-handed lattice vectors in the [Niggli-cell form]({{ site.baseurl }}/pages/definitions/Niggli_defs.html)
- aligned in a particular CASM-standardized direction

If the structure in the `` `prim.json` `` file is not in the canonical form, then `` `casm init` `` will output a new `` `prim.json` ``-style file that you are suggested to use instead.
