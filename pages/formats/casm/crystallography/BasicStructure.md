---
layout: default
---
### BasicStructure

A BasicStructure describes the primitive crystal structure ("prim") and defines the allowed degrees of freedom. It lists lattice vectors, crystal basis sites, global degrees of freedom, and site degrees of freedom, including   allowed occupant species on each basis site.


### JSON format:

- `title`: string

  A title for the project. Must consist of alphanumeric characters and underscores only. The first character may not be a number.   

- `lattice_vectors`: 3x3 array of numbers

  Lattice vectors (as row vectors) for the primitive structure, in Angstroms.

  Example:

      "lattice_vectors": [
        [ 4.0, 0.0, 0.0], // lattice vector 1
        [ 0.0, 4.0, 0.0], // lattice vector 2
        [ 0.0, 0.0, 4.0], // lattice vector 3
      ]

- `coordinate_mode`: string

  Coordinate mode for basis sites. One of:                         
  - "Fractional" or "Direct",                                  
  - "Cartesian"                                                  

- `dofs`: JSON dictionary of DoF JSON objects (optional)

  For each allowed type of global site DoF (typically strain), an object specifying how it is defined. See "DoF JSON object" format below.

- `basis`: array of objects                            

  - `coordinate`: size 3 array of numbers                       

    Coordinate of the basis site with units as specified by the `coordinate_mode` parameter. The default tolerance for checking symmetry is 1e-5, so basis site coordinates should include 6 significant digits or more.                          

  - `occupants`: array of string

    A list of the possible occupant species that may reside at each site. The names are case sensitive, and "Va" is reserved for vacancies.                                                     

  - `dofs`: JSON object (optional):   

    For each allowed type of site DoF (e.g., displacement, magnetic spin, etc.) an object specifying how it is defined. See "DoF JSON object" format below.

- `species`: object (optional)[OPTIONAL]

  A dictionary used to define extended attributes of any species listed as an allowed occupant in `"basis"/"occupants"`.


#### DoF JSON object:

DoFs are continuous vectors having a standard basis that is related to the fixed reference frame of the crystal. The DoF object encodes a user-specified basis in terms of the standard basis. User-specified basis may fully span the standard basis or only a subspace. Within a `"dofs"` object, each DoF is given by the key/object pair `"<dofname>" : {...}` where `<dofname>` is the name specifier of a particular DoF type and the associated object specifies non-default options.

Example: Site displacement DoF:

    "disp" : {
      "axis_names" : ["dxy", "dz"],
      "basis" : [
        [1.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
      ]
    }

Allowed site DoF include:

- "disp": atomic displacement

Allowed global DoF include:

- "GLstrain": Grenn-Lagrange strain metric
- "Hstrain": Hencky strain metric
- "Bstrain": Biot strain metric
- "Ustrain": Stretch tensor, U, where displacement gradient F = R * U
- "EAstrain": Euler-Almansi strain metric


#### Molecule JSON object:

Used to define species the comprise multiple atoms, off-centered
atoms, or species with attributes such as a magnetic spin or or
charge state.

Allowed fields:

- `name`: string (optional)

  Chemical name of molecule, used to override its name in the enclosing dictionary. This name is used for chemical comparisons of molecules. Crystallographic and spatial comparisons are not dependent on molecule names.

- `atoms`: array of object

  Each atom object has the following properties:

  - `name`: string
    Name of atomic species.

  - `coordinate`: size 3 array of number

    Position of the atom, relative to the basis site at which it
    is placed. Coordinate mode is same as rest of `prim.json`.

  - `attributes`: object of SpeciesAttribute (optional)

    Additonal fixed attributes of the atom, such as magnetic moment,
    charge state, or selective dynamics flags. The name of each
    attribute must correspond to a CASM-supported SpeciesAttribute.

- `attributes`: object of SpeciesAttribute (optional)

  Additonal fixed attributes of the molecule as a whole, such as
  magnetic spin, charge state, or selective dynamics flags. The
  name of each attribute must correspond to a CASM-supported
  SpeciesAttribute.


#### SpeciesAttribute JSON object:

Associates the discrete value of a vector property to an Atom or Moleule.

Allowed fields:

- `value`: array of number

  Dimension of array must match the dimension of the specified
  SpeciesAttribute.


### Examples

Example 1, FCC ternary alloy of elements A, B, and C
```
{
  "basis" : [
    {
      "coordinate" : [ 0.000000000000, 0.000000000000, 0.000000000000 ],
      "occupants" : [ "A", "B", "C" ]
    }
  ],
  "coordinate_mode" : "Fractional",
  "description" : "Face-centered Cubic (FCC, cF)",
  "lattice_vectors" : [
    [ 2.000000000000, 2.000000000000, 0.000000000000 ],
    [ 0.000000000000, 2.000000000000, 2.000000000000 ],
    [ 2.000000000000, 0.000000000000, 2.000000000000 ]
  ],
  "title" : "ABC"
}
```

Example 2, FCC binary alloy of elements A and B with Green-Lagrange strain DoF
```
{
  "basis" : [
    {
      "coordinate" : [ 0.000000000000, 0.000000000000, 0.000000000000 ],
      "occupants" : [ "A", "B" ]
    }
  ],
  "dofs" : {
    "GLstrain" : {},
  }
  "coordinate_mode" : "Fractional",
  "description" : "Face-centered Cubic (FCC, cF)",
  "lattice_vectors" : [
    [ 2.000000000000, 2.000000000000, 0.000000000000 ],
    [ 0.000000000000, 2.000000000000, 2.000000000000 ],
    [ 2.000000000000, 0.000000000000, 2.000000000000 ]
  ],
  "title" : "AB_with_Strain"
}
```

Example 3, Zincblende GaAs with Hencky strain DoF along (x,x), (y,y), and (z,z) components
```
{
  "basis" : [
    {
      "coordinate" : [ 0.000000000000, 0.000000000000, 0.000000000000 ],
      "occupants" : [ "Ga" ]
    },
    {
      "coordinate" : [ 0.250000000000, 0.250000000000, 0.250000000000 ],
      "occupants" : [ "As" ]
    }
  ],
  "dofs" : {
    "Hstrain" : {
      "axis_names" : [ "Exx", "Eyy", "Ezz" ],
      "basis" : [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                   [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                   [0.0, 0.0, 1.0, 0.0, 0.0, 0.0]]
    },
  }
  "coordinate_mode" : "Fractional",
  "description" : "Zincblende GaAs with deviatoric strain",
  "lattice_vectors" : [
    [ 0.00000, 2.82663, 2.82663 ],
    [ 2.82663, 0.00000, 2.82663 ],
    [ 2.82663, 2.82663, 0.00000 ]
  ],
  "title" : "GaAs"
}
```

Example 4, BCC lithium with atomic displacement DoF
```
{
  "basis" : [
    {
      "coordinate" : [ 0.000000000000, 0.000000000000, 0.000000000000 ],
      "dofs" : {
        "disp" : {},
      }
      "occupants" : [ "Li" ]
    }
  ],
  "coordinate_mode" : "Fractional",
  "description" : "Body-centered Cubic (BCC, cI)",
  "lattice_vectors" : [
    [ -1.75445,  1.75445,  1.75445 ],
    [  1.75445, -1.75445,  1.75445 ],
    [  1.75445,  1.75445, -1.75445 ]
  ],
  "title" : "Li_with_displacement"
}
```

Example 5, HCP Zr with O insertion at octahedral interstitial positions
```
{
  "basis" : [
    {
      "coordinate" : [ 0.0, 0.0, 0.0 ],
      "occupants" : [ "Zr" ]
    },
    {
      "coordinate" : [ 0.666666, 0.333333, 0.5 ],
      "occupants" : [ "Zr" ]
    },
    {
      "coordinate" : [ 0.333333, 0.666666, 0.25 ],
      "occupants" : [ "Va", "O" ]
    },
    {
      "coordinate" : [ 0.333333, 0.666666, 0.75 ],
      "occupants" : [ "Va", "O" ]
    }
  ],
  "coordinate_mode" : "Fractional",
  "description" : "hcp Zr with oct (O) ",
  "lattice_vectors" : [
    [  3.233986860000, 0.000000000000, 0.000000000000 ],
    [ -1.616993430000, 2.800714770000, 0.000000000000 ],
    [ -0.000000000000, 0.000000000000, 5.168678340000 ]
  ],
  "title" : "ZrO"
}
```
