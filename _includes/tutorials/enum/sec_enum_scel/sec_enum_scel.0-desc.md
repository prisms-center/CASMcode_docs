In CASM, crystal states consistent with the primitive crystal structure are called "configurations". Each configuration can be represented by specifying:

- supercell vectors used to repeat a unit cell into the infinite crystal
- the value of local degrees of freedom at each site in the unit cell, including:
  - discrete site DoF (atom or molecule site occupant)
  - continuous site DoF (ex: displacement vector)
- the value of global degrees of freedom (ex: strain)

Each CASM project contains a database of enumerated supercells and configurations, which may have been generated in a variety of different ways. The primary approach is to enumerate them directly using methods accessed via the `` `casm enum` `` subcommand.

From within a CASM project, the list of enumeration methods can be printed using `` `casm enum -h` ``.
