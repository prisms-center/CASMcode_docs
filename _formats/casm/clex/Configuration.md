---
title: "Configuration"
permalink: /formats/casm/clex/Configuration/
---

### Description

A representation of a single crystal state, defined by the specification of degrees of freedom (DoF) values in a supercell of a [Prim].


#### Project files

This format is used for the [`config.json`] file, which may be generated using the `casm query --write-config` method.

### JSON Attributes List

Configuration attributes:

| Name | Description | Format |
|-|-|-|
| [`dof`](#dof) | DoF values | [ConfigDoF](#configdof-json-object) |
| [`supercell_name`](#supercell-name) | Supercell name | string |
| [`transformation_matrix_to_supercell`](#transformation-matrix-to-supercell) | Transformation matrix from prim to supercell lattice vectors | 2d array of int |

---

ConfigDoF attributes:

| Name | Description | Format |
|-|-|-|
| [`occ`](#occ) | Occupation values | array of int |
| [`local_dofs`](#local-dofs) | Continuous site DoF values | dict |
| [`global_dofs`](#global-dofs) | Continuous global DoF values | dict |

---

Configuration state attributes:

| Name | Description | Format |
|-|-|-|
| [`configuration`](#state-configuration) | Configuration | [Configuration] |
| [`sites`](#state-sites) | Selected sites | array of int |


### JSON Attributes Description

#### Configuration JSON object

- {: #dof } `dof`: [ConfigDoF](#configdof-json-object) (optional)

  Specifies DoF values for this configuration.

  When reading a Configuration from JSON, if `dof` is not present the default configuration (with all DoF values equal 0) will be used. If `dof` is present, then it is required to include values for all DoF defined in the [prim].

- {: #supercell-name } `supercell_name`: string (optional)

  The name of the supercell.

  If the supercell lattice is in [canonical form], the name has the format `"SCELV_A_B_C_D_E_F"`, where `V` is the integer supercell volume (as a multiple of the primitive cell volume), and `"A_B_C_D_E_F"` are integer values of the hermite normal form of the `transformation_matrix_to_supercell` matrix. If the supercell is not in canonical form, the name has the format `"SCELV_A_B_C_D_E_F.G"`, where `G` is the index in the [prim] factor group of an operation that transforms the supercell lattice vectors in canonical form to the supercell lattice vector in its current form.

  When reading a Configuration from JSON, CASM determines the supercell from `transformation_matrix_to_supercell` only and `supercell_name` is ignored.

- {: #transformation-matrix-to-supercell } `transformation_matrix_to_supercell`: 2d array of int (required, `shape=(3,3)`)

  The matrix that transforms the [prim] lattice vectors into the supercell lattice vectors, according to $S = P * T$, where $S$ is the supercell lattice vectors as a column vector matrix, $P$ is the [prim] lattice vectors as a column vector matrix, and $T$ is `transformation_matrix_to_supercell`.


#### ConfigDoF JSON object

Specifies DoF values for a configuration. Required to include values for all DoF defined in the [prim].

- {: #occ } `occ`: array of int (required)

  Occupation DoF values are represented by an array of integers, of size equal to the number of sites in the supercell, and sorted by sublattice. The integer value is the index into the [occupants list] of the sublattice the site is a part of.

  <div>
  **Example:** Occupation values for a configuration of in a volume 8 supercell of a prim with 2 basis sites

      //     |<- sublattice 0 ----->| <- sublattice 1 ----->]
      "occ": [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]

  </div>
  {: .notice--info }

   Within the block of a particular sublattice, values are ordered by the same unit cell ordering.

   **Note:** For a given supercell, the `casm info -m SupercellInfo` method can be used to obtain information about the supercell, including the coordinates of sites in the supercell (from the `cart_coordinate`, `frac_coordinate`, or `integral_site_coordinates` properties) and the order of unit cells within the block of a particular sublattice (from the `unitcells` property).
   {: .notice--info}

- {: #local-dofs } `local_dofs`: dict

  The values of the continuous site DoF.

  Each row corresponds to a site (in the same order as the [`occ`](#occ) values), and contains the site DoF value as a vector in the [standard basis].

  **Note:** Whether or not a user-specified basis is given in the [prim], `local_dofs` values are always written to JSON using the standard basis. When reading a Configuration from JSON, CASM transforms values from the standard basis into the user-specified basis for internal use.
  {: .notice--info}

  <div>
  **Example:** Displacement values in the standard basis, $[d_x, d_y, d_z]$, for a configuration with 4 sites

      "local_dofs" : {
        "disp" : {
          "values" : [
            [  0.100000000000,  0.100000000000, 0.000000000000 ],
            [ -0.100000000000, -0.100000000000, 0.000000000000 ],
            [  0.100000000000, -0.100000000000, 0.000000000000 ],
            [ -0.100000000000,  0.100000000000, 0.000000000000 ]
          ]
        }
      }

  </div>
  {: .notice--info }

- {: #global-dofs } `global_dofs`: dict

  The values of the continuous global DoF, represented as a vector in the [standard basis].

  **Note:** Whether or not a user-specified basis is given in the [prim], `global_dofs` values are always written to JSON using the standard basis. When reading a Configuration from JSON, CASM transforms values from the standard basis into the user-specified basis for internal use.
  {: .notice--info}

  <div>
  **Example:** Green-Lagrange strain metric values in the [standard basis], $[E_{xx}, E_{yy}, E_{zz}, \sqrt(2)E_{yz}, \sqrt(2)E_{xz}, \sqrt(2)E_{xy}]$, $E=\frac{1}{2}(C-I)$

      "global_dofs" : {
        "GLstrain" : {
          "values" : [ 0.100000000000, 0.100000000000, 0.100000000000, 0.000000000000, 0.000000000000, 0.000000000000 ]
        }
      }

  </div>
  {: .notice--info }

#### Configuration State JSON object

A Configuration and set of selected sites, used as an input to several CASM methods.

- {: #state-configuration } `configuration`: [Configuration](#configuration-json-object)

  A [Configuration](#configuration-json-object).

- {: #state-sites } `sites`: array of int

  An array of indices of selected sites, ordered as described for the [`occ`](#occ) values.


### Examples

#### Example 1) Configuration with occupation only

    {
      "dof" : {
        "occ" : [ 1, 0, 0, 0 ]
      },
      "supercell_name" : "SCEL4_2_2_1_1_1_0",
      "transformation_matrix_to_supercell" : [
        [ -1, 1, 1 ],
        [ 1, -1, 1 ],
        [ 1, 1, -1 ]
      ]
    }

#### Example 2) Configuration with occupation, displacement, and strain DoF

    {
      "dof" : {
        "global_dofs" : {
          "GLstrain" : {
            "values" : [ 0.010000000000, 0.010000000000, 0.010000000000, 0.000000000000, 0.000000000000, 0.000000000000 ]
          }
        },
        "local_dofs" : {
          "disp" : {
            "values" : [
              [ 0.000000000000, 0.000000000000, 0.000000000000 ],
              [ 0.000000000000, 0.000000000000, 0.000000000000 ],
              [ 0.000000000000, 0.000000000000, 0.000000000000 ],
              [ 0.000000000000, 0.000000000000, 0.000000000000 ]
            ]
          }
        },
        "occ" : [ 2, 2, 2, 1 ]
      },
      "supercell_name" : "SCEL4_4_1_1_0_2_1",
      "transformation_matrix_to_supercell" : [
        [ -1, 1, 1 ],
        [ 1, -1, 1 ],
        [ 1, 1, -2 ]
      ]
    }

[canonical form]: {{ "/formats/lattice_canonical_form" |  relative_url }}
[standard basis]:  {{ "/formats/casm/crystallography/BasicStructure#dof-list" |  relative_url }}
[prim basis]:  {{ "/formats/casm/crystallography/BasicStructure#user-specified-dof-basis" |  relative_url }}

{% include file_formats_and_locations.md %}
