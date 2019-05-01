The only input needed to initialize a CASM project is a `` `prim.json` `` file specifying the primitive crystal structure. It includes the lattice vectors, basis site coordinates, and allowed degrees of freedom.

CASM allows three types of degrees of freedom (DoF):

- Discrete site DoF, 1 per site
- Continuous site DoF, >=0 per site
- Continuous global DoF, >=0

_Note: The public version v0.3.X of CASM is currently limited to discrete site DoF._

|![prim_file]({{ site.baseurl }}/assets/tutorials/init/prim_file.png){:width="650px"}|
|`` `prim.json` `` file format|

To get a description of the `` `prim.json` `` file and a couple examples, do:
