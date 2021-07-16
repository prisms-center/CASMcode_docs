---
title: "Structure"
permalink: /formats/casm/crystallography/SimpleStructure/
---

### Description

A representation of a crystal of molecular and/or atomic occupants, and any additional properties.

Both enumerated configurations (as `structure.json` files) and calculation results (as `properties.calc.json` files) may be represented using this format.

**Note**: The positions of atoms or molecules in the crystal state is defined by the lattice vectors (`lattice_vectors`) and atom coordinates (`atom_coords`) or molecule coordinates (`mol_coords`). Strain and displacement properties, which are defined in reference to an ideal state, should be interpreted as the strain and displacement that takes the crystal from the ideal state to the state specified by `lattice_vectors` and `atom_coords` or `mol_coords`. The convention used by CASM is that displacements are applied first, and then the displaced coordinates and lattice vectors are strained.
{: .notice--info}

#### Project files

This format is used for the following standard CASM project files:
- [`structure.json`][]: These files may be generated for [Configuration] using `casm query --write-structure` method.
- [`properties.calc.json`][]: Calculation results from supported software packages may be converted to [`properties.calc.json`] files using `casm calc --report`.

### JSON Attributes List

Structure attributes:

| Name | Description | Format |
|-|-|-|
| [`atom_coords`](#atom-coords) | Atom coordinates | array of coordinate |
| [`atom_type`](#atom-type) | Atom type names | array of string |
| [`atom_properties`](#atom-properties) | Atom properties | dict |
| [`coord_mode`](#coord-mode) | Coordinate type | string |
| [`lattice_vectors`](#lattice) | Lattice vectors | 2d array of number |
| [`mol_coords`](#mol-coords) | Molecule coordinates | array of coordinate |
| [`mol_type`](#mol-type) | Molecule type names | array of string |
| [`mol_properties`](#mol-properties) | Molecule properties | dict |
| [`global_properties`](#global-properties) | Global crystal properties | dict |


### JSON Attributes Description

#### Structure JSON object

- {: #atom-coords } `atom_coords`: array of coordinate (required, `shape=(n_atoms, 3)`)

  An array of atom coordinates.

- {: #atom-type } `atom_type`: array of string (optional, `shape=(n_atoms, 3)`)

  An array of atom type names.

- {: #atom-properties } `atom_properties`: dict (optional, `shape=(n_atoms, standard_dim)`)

  Values of properties associated with particular atoms. Property names are expected to follow the [property naming convenctions] for [standard CASM property types]. Values are input as arrays of vectors, one vector for each atom. Vector dimensions should match the standard basis dimension of the property type.

  The names `atom_dofs`, `atom_vals`, and `atom_values` are accepted as aliases for `atom_properties`.

  Example: Atomic displacements for a structure with 2 atoms

      "atom_properties": {
        "disp": {
          "value": [
            [0.0, 0.1, 0.0],
            [0.0, -0.1, 0.0]
          ]
        }
      }

- {: #coord-mode } `coord_mode`: string (required)

  Coordinate mode for `atom_coords` and `mol_coords`. One of:
  - "Fractional" or "Direct",                                  
  - "Cartesian"                                                  

- {: #lattice-vectors } `lattice_vectors`: 2d array of number, `shape=(3,3)` (required)

  Lattice vectors (as row vectors), in Angstroms.

  Example:

      "lattice_vectors": [
        [ 4.0, 0.0, 0.0], // lattice vector 1
        [ 0.0, 4.0, 0.0], // lattice vector 2
        [ 0.0, 0.0, 4.0], // lattice vector 3
      ]

- {: #mol-coords } `mol_coords`: array of coordinate (required, `shape=(n_molecules, 3)`)

  An array of molecules.

- {: #mol-type } `mol_type`: array of string (optional, `shape=(n_molecules, 3)`)

  An array of molecule type names.

- {: #mol-properties } `mol_properties`: dict (optional)

  Values of properties associated with particular molecules. Property names are expected to follow the [property naming convenctions] for [standard CASM property types]. Values are input as arrays of vectors, one vector for each molecule. Vector dimensions should match the standard basis dimension of the property type.

  The names `mol_dofs`, `mol_vals`, and `mol_values` are accepted as aliases for `mol_properties`.

  Example: Molecular displacements for a structure with 2 molecules

      "mol_properties": {
        "disp": {
          "value": [
            [0.0, 0.1, 0.0],
            [0.0, -0.1, 0.0]
          ]
        }
      }

- {: #global-properties } `global_properties`: dict (optional)

  Values of properties associated with the entire crystal. Property names are expected to follow the [property naming convenctions] for [standard CASM property types]. Values are input as a scalar or vector. Vector dimensions should match the standard basis dimension of the property type.

  The names `global_dofs`, `global_vals`, and `global_values` are accepted as aliases for `global_properties`.

  Example: Crystal with calculated energy

      "global_properties": {
        "energy": {
          "value": 0.1
        }
      }

  Example: Crystal with calculated strain

      "global_properties": {
        "Ustrain": {
          "value": [0.1, 0.1, 0.1, 0.0, 0.0, 0.0]
        }
      }

### Examples

#### Example 1) Structure with occupation and energy

    {
      "atom_coords" : [
        [ 0.000000000000, 0.000000000000, 0.000000000000 ],
        [ 1.754750223661, -1.754750223661, 0.000000000000 ],
        [ 1.754750223661, 0.000000000000, 1.754750223661 ],
        [ 1.754750223661, 1.754750223661, 0.000000000000 ]
      ],
      "atom_type" : [ "C", "B", "B", "A" ],
      "coord_mode" : "Cartesian",
      "global_properties" : {
        "energy" : {
          "value" : 17.003
        }
      },
      "lattice" : [
        [ 1.754750223661, 0.000000000000, -1.754750223661 ],
        [ 1.754750223661, 3.509500447322, 1.754750223661 ],
        [ 1.754750223661, -3.509500447322, 1.754750223661 ]
      ]
    }

#### Example 2) Structure with occupation, displacement, and strain

    {
      "atom_coords" : [
        [ 0.000000000000, 0.000000000000, 0.000000000000 ],
        [ 1.754750223661, -1.754750223661, 0.000000000000 ],
        [ 1.754750223661, 0.000000000000, 1.754750223661 ],
        [ 1.754750223661, 1.754750223661, 0.000000000000 ]
      ],
      "atom_properties" : {
        "disp" : {
          "value" : [
            [ 0.000000000000, 0.000000000000, 0.000000000000 ],
            [ 0.000000000000, 0.000000000000, 0.000000000000 ],
            [ 0.000000000000, 0.000000000000, 0.000000000000 ],
            [ 0.000000000000, 0.000000000000, 0.000000000000 ]
          ]
        }
      },
      "atom_type" : [ "C", "B", "B", "A" ],
      "coord_mode" : "Cartesian",
      "global_properties" : {
        "GLstrain" : {
          "value" : [ 0.000000000000, 0.000000000000, 0.000000000000, 0.000000000000, 0.000000000000, 0.000000000000 ]
        }
      },
      "lattice" : [
        [ 1.754750223661, 0.000000000000, -1.754750223661 ],
        [ 1.754750223661, 3.509500447322, 1.754750223661 ],
        [ 1.754750223661, -3.509500447322, 1.754750223661 ]
      ]
    }

[property naming convenctions]: {{ "/formats/dof_and_properties#property-naming" | relative_url }}
[standard CASM property types]: {{ "/formats/dof_and_properties#properties-list" | relative_url }}

{% include file_formats_and_locations.md %}
