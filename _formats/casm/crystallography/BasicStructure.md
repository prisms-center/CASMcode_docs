---
title: "BasicStructure (\"prim.json\")"
permalink: /formats/casm/crystallography/BasicStructure/
---

A primitive crystal structure and allowed degrees of freedom (DoF), or "prim",  specifies lattice vectors, crystal basis sites, discrete site DoF (occupation DoF), continuous site DoF, and continuous global DoF. A "prim" is represented by CASM internally using the BasicStructure class.


### JSON Attributes

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

  For each allowed type of continuous global DoF (typically strain), an object specifying how it is defined. See ["DoF JSON object" format](#dof-json-object).

- `basis`: array of objects                            

  - `coordinate`: size 3 array of numbers                       

    Coordinate of the basis site with units as specified by the `coordinate_mode` parameter. The default tolerance for checking symmetry is 1e-5, so basis site coordinates should include 6 significant digits or more.                          

  - `occupants`: array of string

    A list of the possible occupant species that may reside at each site. The names are case sensitive, and "Va" is reserved for vacancies.                                                     

  - `dofs`: JSON object (optional):   

    For each allowed type of site DoF (e.g., displacement, magnetic spin, etc.) an object specifying how it is defined. See ["DoF JSON object" format](#dof-json-object).

- `species`: object (optional)

  A dictionary used to define extended attributes of any species listed as an allowed occupant in `"basis"/"occupants"`. See ["Molecule JSON object" format](#molecule-json-object).


#### DoF JSON object

DoFs are continuous vectors having a standard basis that is related to the fixed reference frame of the crystal. The DoF object encodes a user-specified basis in terms of the standard basis. User-specified basis may fully span the standard basis or only a subspace. Within a `"dofs"` object, each DoF is given by the key/object pair `"<dofname>" : {...}` where `<dofname>` is the name specifier of a particular DoF type and the associated object specifies non-default options.

- `axis_names`: array of string

  Provides names for individual DoF when printing basis function formulas. Must match the number of rows in `basis`.

- `basis`: dim x standard_dim array of numbers

  A row-vector matrix defining the user-specified "prim basis" for a site or global DoF in terms of the "standard basis".

Example: Site displacement DoF:

    "disp" : {
      "axis_names" : ["d1", "d2"],
      "basis" : [
        [0.70710678, 0.70710678, 0.0],
        [0.0,        0.0,        1.0]
      ]
    }

Allowed site DoF include:

- "disp": atomic displacement
  - standard basis: ["dx", "dy", "dz"]

Allowed global DoF include:

- Strain, using one of the following metrics:

  - "GLstrain": Grenn-Lagrange strain metric, $\frac{1}{2}(C-I)$
  - "Hstrain": Hencky strain metric, $\frac{1}{2}ln(C)$
  - "Bstrain": Biot strain metric, $(U-I)$
  - "Ustrain": Stretch tensor, $U$
  - "EAstrain": Euler-Almansi strain metric, $\frac{1}{2}(I-(F F^{T})^{-1})$

  The strain metrics are defined in terms of the deformation gradient tensor, $F$, and Green's deformation tensor, $C$. The deformation gradient tensor relates the strained and unstrained lattices through $L^{strained} = F * L^{ideal}$, where $L$ is a column-vector matrix of the lattice vectors. The deformation matrix tensor can be decomposed, via $F = R * U$, into a rotation tensor, $R$, and stretch tensor, $U$. Green's deformation tensor, $C = F^{T}*F$, excludes rigid rotations.

  For all strain metrics, the standard basis is $[E_{xx}, E_{yy}, E_{zz}, \sqrt(2)E_{xz}, \sqrt(2)E_{yz}, \sqrt(2)E_{xy}]$, and the default axis names are ["e_1", "e_2", "e_3", "e_4", "e_5", "e_6"].

For complete documentation of implemented DoF types see the C++ documentation of the [AnisoValTraits] class.

#### Molecule JSON object

Used to define species that are comprised of multiple atoms, off-centered
atoms, or species with attributes such as a magnetic spin or or
charge state.

Allowed fields:

- `name`: string (optional)

  Chemical name of the species, used to override its name in the enclosing dictionary. This name is used for chemical comparisons of molecules. Crystallographic and spatial comparisons are not dependent on molecule names.

- `atoms`: array of object (optional)

  Defines each atomic component of a multiple atom occupant. May be excluded if the species is atomic. Each atom object in the array has the following properties:

  - `name`: string
    Name of atomic species.

  - `coordinate`: size 3 array of number

    Position of the atom, relative to the basis site at which it
    is placed. Coordinate mode is same as rest of `prim.json`.

  - `attributes`: object of SpeciesAttribute (optional)

    Additonal fixed attributes of the atom, such as magnetic moment,
    charge state, or selective dynamics flags. The name of each
    attribute must correspond to a CASM-supported [AnisoValTraits] object type.

- `attributes`: object of SpeciesAttribute (optional)

  Additonal fixed attributes of the molecule as a whole, such as
  magnetic spin, charge state, or selective dynamics flags. The
  name of each attribute must correspond to a CASM-supported
  [AnisoValTraits] object type.


#### SpeciesAttribute JSON object:

Associates the discrete value of a vector property to an Atom or Moleule.

Allowed fields:

- `value`: array of number

  Dimension of array must match the dimension of the specified
  SpeciesAttribute. See [Example 6](#example-6).


### Examples

#### Example 1) FCC ternary alloy of elements A, B, and C
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

#### Example 2) FCC binary alloy of elements A and B with Green-Lagrange strain DoF
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

#### Example 3) Zincblende GaAs with Hencky strain DoF along (x,x), (y,y), and (z,z) components
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

#### Example 4) BCC lithium with atomic displacement DoF
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

#### Example 5) HCP Zr with Va/O at octahedral interstitial positions
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

#### Example 6) Cubic ZrH<sub>2</sub>, with Green-Lagrange strain and selectivedynamics <a id='example-6'></a>

```
{
  "basis" : [
    {
      "coordinate" : [ 0.0000000, 0.0000000, 0.0000000 ],
      "occupant_dof" : [ "Zr" ],
      "dofs": {
        "disp": {}
      }
    },
    {
      "coordinate" : [ 0.2500000, 0.2500000, 0.2500000 ],
      "occupant_dof" : [ "H" ]
    },
    {
      "coordinate" : [ 0.7500000, 0.7500000, 0.7500000 ],
      "occupant_dof" : [ "H" ]
    }
  ],
  "species" : {
    "H": {
      "attributes": {
        "selectivedynamics": {
          "value": [1, 1, 1]
        }
      }
    },
    "Zr": {
      "attributes": {
        "selectivedynamics": {
          "value": [0, 0, 0]
        }
      }
    }
  },
  "dofs" : {
      "GLstrain" : {}
  },
  "coordinate_mode" : "Fractional",
  "description" : "Cubic ZrH_{2}",
  "lattice_vectors" : [
    [0.       , 2.4106965, 2.4106965],
    [2.4106965, 0.       , 2.4106965],
    [2.4106965, 2.4106965, 0.       ]
  ],
  "title" : "ZrH2"
}
```

[AnisoValTraits]: https://prisms-center.github.io/CASMcode_cppdocs/latest/class_c_a_s_m_1_1_aniso_val_traits.html
