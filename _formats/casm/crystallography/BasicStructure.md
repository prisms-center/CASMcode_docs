---
title: "Prim"
permalink: /formats/casm/crystallography/BasicStructure/
---

### Description

The primitive crystal structure and allowed degrees of freedom (DoF) (the "prim") specifies lattice vectors, crystal basis sites, occupation DoF, continuous site DoF, and continuous global DoF.


#### Project files

This format is used for `prim.json` files.

A user-generated `prim.json` file is used to initialize a CASM project. When the project is initialized, CASM writes a standardized [`prim.json`] file to `<root>/.casm/prim.json`, where `<root>` is the CASM project root directory.

For subsequent project actions, CASM will read the prim from `<root>/.casm/prim.json`, not the user-generated file used to initialize the project. It is not recommended to modify the CASM-generated [`prim.json`] file because that may cause inconsistencies in the project.

### JSON Attributes List

BasicStructure attributes:

| Name | Description | Format |
|-|-|-|
| [`basis`](#basis) | Basis site descriptions | array of [Site](#site-json-object) |
| [`coordinate_mode`](#coordinate-mode) | Basis site coordinate type | string |
| [`description`](#description) | Project description | string |
| [`dofs`](#global-dofs) | Continuous global DoF  | dict of [DoF](#degrees-of-freedom-dof-json-object) |
| [`lattice_vectors`](#lattice-vectors) | Lattice vectors | 2d array of number |
| [`species`](#species) | Fixed atom attributes and molecule definitions | dict of [Molecule](#molecule-json-object) |
| [`title`](#title) | Project title | string |

---

Site attributes:

| [`coordinate`](#site-coordinate) | Site coordinate | array of number |
| [`occupants`](#site-occupants) | Site allowed occupants | array of string |
| [`dofs`](#site-dofs) | Continuous site DoF | dict of [DoF](#degrees-of-freedom-dof-json-object)  |

---

DoF attributes:

| Name | Description | Format |
|-|-|-|
| [`axis_names`](#dof-axis-names) | User-specified axis names | array of string |
| [`basis`](#dof-basis) | User-specified DoF basis | 2d array of number |

---

Molecule attributes:

| Name | Description | Format |
|-|-|-|
| [`atoms`](#molecule-atoms) | List of atoms that comprise a molecule | array of [Atom Component](#atom-component-json-object) |
| [`attributes`](#molecular-attributes) | Fixed molecular attributes | dict of [Species Attribute](#species-attribute-json-object)  |
| [`name`](#molecule-chemical-name) | Chemical name | string |

---

Atom Component attributes:

| [`name`](#atom-name) | Atom name | string |
| [`coordinate`](#atom-coordinate) | Atom coordinate, relative to site location | array of number |
| [`attributes`](#atomic-attributes) | Fixed atomic attributes | dict of [Species Attribute](#species-attribute-json-object) |

---

Species Attribute attributes:

| [`value`](#species-attribute-value) | Species attribute value |


### JSON Attributes Description

#### BasicStructure JSON object

- {: #basis } `basis`: array of [Site](#site-json-object) (required, `shape=(n_sublattice,)`)

  An array of [Site](#site-json-object) objects that specifies the coordinate, allowed occupants, and allowed continuous site DoF for each sublattice of the crystal. The size of the `basis` array defines the number of sublattices in the crystal (`n_sublattice`). Elsewhere, the variables `sublattice_index` or `b` (in the "integral site coordinate" convention), are used to indicate a particular sublattice.

  Example:

- {: #coordinate-mode } `coordinate_mode`: string (required)

  Coordinate mode for basis sites. One of:                         
  - "Fractional" or "Direct",                                  
  - "Cartesian"                                                  

- {: #description } `description`: string (optional)

  An extended description for the project. Included by convention in most example `prim.json` files, this attribute is not read by CASM.

- {: #global-dofs } `dofs`: dict (optional, `default={}`)

  A dictionary specifying the types of continuous global DoF and their basis. For more details on the allowed global DoF types and specifiying the standard or user-specified basis, see [DoF](#degrees-of-freedom-dof-json-object).

  Example: Strain DoF, using the Hencky strain metric, with standard basis:

      "dofs": {
        "Hstrain" : {}
      }

  Example: Strain DoF, using the Hencky strain metric, with user-specified basis:

      "dofs": {
        "Hstrain" : {
          "axis_names": ["e_1", "e_2", "e_3"],
          "basis" : [
            [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
          ]
        }
      }

- {: #lattice-vectors } `lattice_vectors`: 2d array of number, `shape=(3,3)` (required)

  Lattice vectors (as row vectors), in Angstroms.

  Example:

      "lattice_vectors": [
        [ 4.0, 0.0, 0.0], // lattice vector 1
        [ 0.0, 4.0, 0.0], // lattice vector 2
        [ 0.0, 0.0, 4.0], // lattice vector 3
      ]

- {: #species } `species`: dict (optional, `default={}`)

  A dictionary used to define fixed attributes of any species listed as an allowed occupant in `"basis/<sublattice_index>/occupants"` that is not a single isotropic atom. Allows for specifying fixed attributes of an atom, such as magnetic spin, or selective dynamics flags, defining molecules, and specifying allowed molecular orientations and fixed molecular attributes. See ["Molecule JSON object" format](#molecule-json-object).

  Example: Specifying selective dynamics by species type

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
      }

- {: #title } `title`: string (required)

  A title for the project. Must consist of alphanumeric characters and underscores only. The first character may not be a number.   


#### Site JSON object

Used to specify the coordinate, allowed occupants, and allowed continuous site DoF for a sublattice in the prim.

- {: #site-coordinate } `coordinate`: array of number, `shape=(3,)` (required)

  Coordinate of the basis site with units as specified by the `coordinate_mode` parameter. The default tolerance for checking symmetry is 1e-5, so basis site coordinates should include 6 significant digits or more.

- {: #site-occupants } `occupants`: array of string (optional, `default=["UNKNOWN"]`)

  A list of the possible occupant species that may reside at each site. The names are case sensitive, and "Va" is reserved for vacancies. If not specified, an `"UNKNOWN"` occupant species is created.

- {: #site-dofs } `dofs`: dict (optional, `default={}`):   

  A dictionary specifying the types of continuous site DoF allowed on this site and their basis. For more details on the allowed site DoF types and specifiying the standard or user-specified basis, see [DoF](#degrees-of-freedom-dof-json-object).

  Example: Atomic displacement, using standard basis

      "dofs": {
        "disp" : {}
      }

  Example: Atomic displacement DoF, with user-specified basis:

      "dofs": {
        "disp": {
          "axis_names": ["d1", "d2"],
          "basis": [
            [0.70710678, 0.70710678, 0.],
            [-0.70710678, 0.70710678, 0.]
          ]
        }
      }


#### Degrees of freedom (DoF) JSON object

Degrees of freedom (DoF) are continuous-valued vectors having a standard basis that is related to the fixed reference frame of the crystal. CASM supports both site DoF, which are associated with a particular prim basis site, and global DoF, which are associated with the infinite crystal. Standard DoF types are implemented in CASM and a traits system allows developers to extend CASM to include additional types of DoF.

##### DoF List

Standard DoF types included in CASM:

{% include dof_list.md %}

##### User-specified DoF basis

In many cases, the standard basis is the appropriate choice, but CASM also allows for a user-specified basis in terms of the standard basis. A user-specified basis may fully span the standard basis or only a subspace. Within a `"dofs"` dict, each DoF is given by the key/object pair `"<dofname>" : {...}` where `<dofname>` is the name specifier of a particular DoF type and the associated object specifies non-default options.

- {: #dof-axis-names } `axis_names`: array of string, `shape=(dim,)` (required if `basis` present)

  Provides names for individual DoF when printing basis function formulas. If `basis` is present, then the size of `axis_names` must match the number of rows in `basis`. The default value is the standard basis, as defined by CASM for each DoF type.

- {: #dof-basis } `basis`: 2d array of number, `shape=(dim, standard_dim)` (optional, default is the standard basis)

  A row-vector matrix defining the user-specified "prim basis" for a site or global DoF in terms of the "standard basis". The default value of `basis` is the "standard basis", which is the identity matrix of shape `(standard_dim, standard_dim)`.

Example: Atomic displacement DoF with user-specified basis:

    "disp" : {
      "axis_names" : ["d1", "d2"],
      "basis" : [
        [0.70710678, 0.70710678, 0.0],
        [0.0,        0.0,        1.0]
      ]
    }

Example: Strain DoF, using the Hencky strain metric, with user-specified basis:

    "Hstrain" : {
      "axis_names": ["e_1", "e_2", "e_3"],
      "basis" : [
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
      ]
    }

#### Molecule JSON object

Used to define species that are comprised of multiple atoms, off-centered
atoms, or species with attributes such as a magnetic spin or selective dynamics flags.

- {: #molecule-atoms } `atoms`: array of [Atom Component](#atom-component-json-object) (optional)

  Defines each atomic component of a multiple atom occupant. May be excluded for single-atom molecules.

- {: #molecular-attributes } `attributes`: dict of [Species Attribute](#species-attribute-json-object) (optional)

  Additonal fixed attributes of the molecule as a whole, such as magnetic spin or selective dynamics flags. The name of each attribute must be a CASM-supported [property] type. The dimension of the `value` array must match the standard dimension of the [property] type.

  Example:

      "attributes": {
        "selectivedynamics": {
          "value": [1, 1, 1]
        }
      }

- {: #molecule-chemical-name } `name`: string (optional)

  Chemical name of the species, used to override its name in the enclosing `species` dictionary. This name is used for chemical comparisons of molecules. Crystallographic and spatial comparisons are not dependent on molecule names.


#### Atom Component JSON object:

Used to define an atom that is a component of a molecule.

- {: #atom-coordinate } `coordinate`: size 3 array of number

  Position of the atom, relative to the basis site at which it is placed. Coordinate mode is same as rest of `prim.json`.

- {: #atomic-attributes } `attributes`: dict of [Species Attribute](#species-attribute-json-object) (optional)

  Additonal fixed attributes of the atom, such as magnetic moment or selective dynamics flags. The name of each attribute must be a CASM-supported [property] type. The dimension of the `value` array must match the standard dimension of the [property] type.

  Example:

      "attributes": {
        "selectivedynamics": {
          "value": [1, 1, 1]
        }
      }

- {: #atom-name } `name`: string
  Name of atomic species.

#### Species Attribute JSON object:

Associates the discrete value of a vector property to an atom or moleule.

- {: #species-attribute-value } `value`: array of number

  The dimension of the `value` array must match the standard dimension of the CASM-supported [property] type whose name is the key for this object. See [Example 6](#example-6).


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
  "title" : "AB_with_GLstrain"
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

[property]: {{ "/formats/dof_and_properties#properties-list" |  relative_url }}

{% include file_formats_and_locations.md %}
