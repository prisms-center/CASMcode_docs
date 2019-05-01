The `` `casm init` `` command generates a number of subdirectories in your CASM project:
- `` `.casm` ``: A hidden directory that identifies the parent directory as a CASM project. The `` .casm` `` directory contains settings and data that the user should generally not need to interact with directly.
- `` `basis_sets` ``: Users create basis set specification files (`` `bspecs.json` ``) inside subdirectories which CASM then parses to construct basis sets and stores data, generated source code, and libraries used to describe and evaluate the basis sets.  
- `` `cluster_expansions` ``: Stores `` `eci.json` `` files containing the basis set coefficients (effective cluster interactions, or ECI) after they have been determined.
- `` `symmetry` ``: Stores files describing the lattice point group, factor group, and crystal point group.
- `` `training_data` ``: Used to hold first-principles calculations input and output.

Attempting to initialize a CASM project that has already been initialized and has a `` `.casm` `` directory results in a message that the project already exists.
