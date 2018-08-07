The `` `casm init` `` command generates a number of subdirectories in your CASM project:
- `` `.casm` ``: A hidden directory that identifies the parent directory as a CASM project. The `` .casm` `` directory contains settings and data that the user should generally not need to interact with directly.
- `` `basis_sets` ``: Users create basis set specification files (`` `bspecs.json` ``) inside subdirectories which CASM then parses to construct basis sets and stores data, generated source code, and libraries used to describe and evaluate the basis sets.  
- `` `cluster_expansions` ``: Stores `` `eci.json` `` files containing the basis set coefficients (effective cluster interactions, or ECI) after they have been determined.
- `` `symmetry` ``: Stores files describing the lattice point group, factor group, and crystal point group.
- `` `training_data` ``: Used to hold first-principles calculations input and output.

It also generates a `` `LOG` `` file which records the steps performed while working on your CASM project. While it is not 100% complete record (it is limited to logging commands performed using the `` `casm` `` program that use the CASM c++ library) it can be useful to remember actions taken.
