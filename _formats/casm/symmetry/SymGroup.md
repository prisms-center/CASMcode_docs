---
title: "Symmetry Group"
permalink: /formats/casm/symmetry/SymGroup/
---

### Description

Contains a description of a symmetry group.


#### Project files

This format is used for all symmetry group files in the CASM project, including the [`lattice_point_group.json`], [`factor_group.json`], and [`crystal_point_group.json`] files.


### JSON Attributes List

Symmetry Group attributes:

| Name | Description | Format |
|-|-|-|
| [`group_classification`](#group-classification) | Group classification information, such as the point group | [Symmetry Group Classification](#symmetry-group-classification-json-object) |
| [`group_operations`](#group-operations) | Descriptions of group operations | dict of [Symmetry Operation](#symmetry-operation-json-object) |
| [`group_structure`](#group-structure) | Multiplication table and conjugacy classes | [Symmetry Group Structure](#symmetry-group-structure-json-object) |

---

Symmetry Group Classification attributes:

| Name | Description | Format |
|-|-|-|
| [`latex_name`](#latex-name) | Point group name, formatted for Latex | string |
| [`name`](#name) | Point group name | string |
| [`periodicity`](#periodicity) | Whether there is translation symmetry | string |

---

Symmetry Operation attributes:

| Name | Description | Format |
|-|-|-|
| [`CART`](#cart-rep) | Cartesian coordinate transformation representation | [Coordinate Transformation Representation](#coordinate-transformation-representation-json-object) |
| [`FRAC`](#frac-rep) | Fractional coordinate transformation representation | [Coordinate Transformation Representation](#coordinate-transformation-representation-json-object) |
| [`info`](#info) | Symmetry operation information | [Symmetry Operation Information](#symmetry-operation-information-json-object) |
| [`master_group_index`](#master-group-index) | Index of this operation in the master group | int |

---

Coordinate Transformation Representation attributes:

| Name | Description | Format |
|-|-|-|
| [`matrix`](#symop-matrix) | Coordinate transformation matrix | 2d array of number |
| [`tau`](#symop-tau) | Coordinate translation vector | array of number |
| [`time_reversal`](#symop-time-reversal) | Whether symmetry includes time reversal invariance | bool |

---

Symmetry Operation Information attributes:

| Name | Description | Format |
|-|-|-|
| [`brief`](#symop-info-brief) | Brief string descriptions of the symmetry operation | dict of string |
| [`conjugacy_class`](#symop-info-conjugacy-class) | Index of the conjugacy class containing the operation | int |
| [`invariant_point`](#symop-info-invariant-point) | Coordinate of an invariant point of the operation | dict |
| [`inverse_operation`](#symop-info-inverse-operation) | Index in the group of the inverse operation | int |
| [`mirror_normal`](#symop-info-mirror-normal) | Unit normal vector of mirror and glide planes | dict |
| [`rotation_angle`](#symop-info-rotation-angle) | Rotation angle of the operation | number |
| [`rotation_axis`](#symop-info-rotation-axis) | Rotation axis of the operation | dict |
| [`shift`](#symop-info-shift) | Screw or glide shift vector | dict |
| [`type`](#symop-info-type) | Type of symmetry operation | string |

---

Symmetry Group Structure attributes:

| Name | Description | Format |
|-|-|-|
| [`conjugacy_classes`](#conjugacy-classes) | Conjugacy class elements and type | dict |
| [`multiplication_table`](#multiplication-table) | Group multiplication table | 2d array of int |


### JSON Attributes Description

#### Symmetry Group JSON Object

- {: #group-classification } `group_classification`: [Symmetry Group Classification][Group Classification](#symmetry-group-classification-json-object)

  Group classification information, such as the point group.

- {: #group-operations } `group_operations`: dict of [Symmetry Operation](#symmetry-operation-json-object)

  Descriptions of group operations. The dictionary keys are of the form `op_01`, `op_02`, ..., or `op_1`, `op_2`, ..., if there are less than 10 elements in the group.

- {: #group-structure } `group_structure`: [Symmetry Group Structure](#symmetry-group-structure-json-object)

  Contains the group multiplication table and conjugacy classes.


#### Symmetry Group Classification JSON Object

- {: #latex-name } `latex_name`: string

   Point group name, formatted for Latex

- {: #name } `name`: string

  Point group name.

- {: #periodicity } `periodicity`: string

  Has the value "PERIODIC" if there is translation symmetry, or the value "APERIODIC" if there is not translation symmetry.


#### Symmetry Operation JSON Object

- {: #cart-rep } `CART`: [Coordinate Transformation Representation](#coordinate-transformation-representation-json-object)

  Cartesian coordinate transformation representation.

- {: #frac-rep } `FRAC`: [Coordinate Transformation Representation](#coordinate-transformation-representation-json-object)

  Fractional coordinate transformation representation

- {: #info } `info`: [Symmetry Operation Information](#symmetry-operation-information-json-object)

   Symmetry operation information

- {: #master-group-index } `master_group_index`: int

  Index of this operation in the master group. The master group is the group from which all subgroups are formed. Most commonly, the master group is the factor group of the [prim].


#### Coordinate Transformation Representation JSON Object

The symmetery operations transform a spatial coordinate $x \\rightarrow x'$ according to $x' = R*x+\tau$, where $R$ is the 3x3 coordinate transformation matrix and $\tau$ is the coordinate translation vector. The values $R$ and $\tau$ for the same symmetry operation may be expressed in either Cartesian or fractional coordinates using the conversion, $x^{cart} = L * x^{frac}$, where $L$ is the lattice vector column matrix.

- {: #symop-matrix } `matrix`: 2d array of number (`shape=(3,3)`)

  Coordinate transformation matrix.

- {: #symop-tau } `tau`: array of number  (`shape=(3,)`)

  Coordinate translation vector.

- {: #symop-time-reversal } `time_reversal`: bool

  Whether symmetry includes time reversal invariance.


#### Symmetry Operation Information JSON Object

- {: #symop-info-brief } `brief`: dict

  Brief string descriptions of the symmetry operation, following the conventions of _(International Tables for Crystallography (2015). Vol. A. ch. 1.4, pp. 50-59)_. Includes Cartesian and fractional coordinate representations.

  <div>
  **Example:**

      "brief" : {
        "CART" : "6⁺ (0.0000000 0.0000000 2.5843392) 0, 1.867143, z",
        "FRAC" : "6⁺ (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z"
      }

  </div>
  {: .notice--info }

  <div>
  **Examples:**

  The following examples are given in the fractional coordinate representation.

  - `1`: Identity operation.

  - `3⁺ 0, 0, z`: Positive 3-fold rotation around the axis with coordinates `0, 0, z`, for any `z`.

  - `2 ( 0.5000000 -0.0000000  0.0000000) x, 0.1666667, 0.25`: 2-fold screw rotation, with shift vector `(0.5000000 -0.0000000  0.0000000)`, around the axis with coordinates `x, 0.1666667, 0.25`, for any `x`.

  - `m x, -x, z`: Mirror plane, with coordinates `x, -x, z`, for any `x`, `z`.

  - `g (0.5000000 0.5000000 0.5000000) 0.08333334+x, -0.08333334+x, z`: Glide reflection, with shift vector `(0.5000000 0.5000000 0.5000000)`, and glide plane with coordinates `0.08333334+x, -0.08333334+x, z` for any `x`, `z`.

  - `-3⁺ 0.3333333, -0.3333333, z;  0.3333333 -0.3333333  0.2500000`: Positive 3-fold rotoinversion around the axis `0.3333333, -0.3333333, z`, for any `z`, and the invariant point `0.3333333 -0.3333333  0.2500000`.

  - `-1 0.3333333 0.1666666 0.2500000`: Inversion, with the invariant point `0.3333333 0.1666666 0.2500000`.

  - `m′ x, y, y`: Mirror plane, with coordinates `x, y, y`, for any `x`, `y`, and time reversal invariance (indicated by the prime).

  </div>
  {: .notice--info }

- {: #symop-info-conjugacy-class } `conjugacy_class`: int

   Index of the [conjugacy class](#conjugacy-classes) containing the operation.

- {: #symop-info-invariant-point } `invariant_point`: dict (conditional)

  Coordinate of an invariant point of the operation, if applicable. Includes Cartesian and fractional coordinate representations.

  <div>
  **Example:**

      "invariant_point" : {
        "CART" : [ 0.000000000000, 1.867143135410, 0.000000000000 ],
        "FRAC" : [ 0.333333325000, 0.666666650000, 0.000000000000 ]
      }

  </div>
  {: .notice--info }

- {: #symop-info-inverse-operation } `inverse_operation`: int

  Index in the group of the inverse operation.

- {: #symop-info-mirror-normal } `mirror_normal`: dict (conditional)

  Unit normal vector of mirror and glide planes, if applicable. Includes Cartesian and fractional coordinate representations.

  <div>
  **Example:**

      "mirror_normal" : {
        "CART" : [ 0.500000000000, -0.866025403784, 0.000000000000 ],
        "FRAC" : [ 0.000000000000, -1.000000000000, 0.000000000000 ]
      }

  </div>
  {: .notice--info }

- {: #symop-info-rotation-angle } `rotation_angle`: number (conditional)

  Rotation angle of the operation, in degrees, if applicable.

- {: #symop-info-rotation-axis } `rotation_axis`: dict (conditional)

  Vector lying along the rotation axis of the operation, if applicable. Includes Cartesian and fractional coordinate representations.

  <div>
  **Example:**

      "rotation_axis" : {
        "CART" : [ 0.500000000000, 0.866025403784, -0.000000000000 ],
        "FRAC" : [ 0.707106781187, 0.707106781187, 0.000000000000 ]
      }

  </div>
  {: .notice--info }

- {: #symop-info-shift } `shift`: dict (conditional)

  Screw or glide shift vector, if applicable. Includes Cartesian and fractional coordinate representations.

  <div>
  **Example:**

      "shift" : {
        "CART" : [ 0.808496714096, 1.400357386566, -0.000000000000 ],
        "FRAC" : [ 0.500000000000, 0.500000000000, 0.000000000000 ]
      }

  </div>
  {: .notice--info }

- {: #symop-info-type } `type`: string

  Type of symmetry operation. One of "identity", "rotation", "screw", "mirror", "glide", "rotoinversion", or "inversion".

#### Symmetry Group Structure JSON Object

- {: #conjugacy-classes } `conjugacy_classes`: dict

  [Conjugacy class](https://en.wikipedia.org/wiki/Conjugacy_class) operations, type, and rotation angle (if applicable).

  <div>
  **Example:**

      "conjugacy_classes" : {
        "class_01" : {
          "operation_type" : "identity",
          "operations" : [ 1 ]
        },
        "class_02" : {
          "operation_type" : "screw",
          "operations" : [ 2, 3 ],
          "rotation_angle" : 60.000000000000
        },
        "class_03" : {
          "operation_type" : "rotation",
          "operations" : [ 4, 5 ],
          "rotation_angle" : 120.000000000000
        },
        ...
      }

  </div>
  {: .notice--info }

- {: #multiplication-table } `multiplication_table`: 2d array of int

  Group multiplication table. The symmetry operation products $g_k = g_i g_j$ are specified by $M_{ij}=k$, where $g_i$, $g_j$, and $g_k$ are the $i$-th, $j$-th, and $k$-th symmetry operations in the group, and $M$ is the multiplication table.


### Examples

Example Symmetry Group files:
1. Factor group, for HCP Zr, with octahedral interstitial O disorder: [[factor_group_ex1.json]]({{ "/assets/example_files/factor_group_ex1.json" | relative_url }})
2. Factor group, for an FCC system with collinear magnetic spin (`Cmagspin`) [DoF] (which has time reversal symmetry): [[factor_group_ex2.json]]({{ "/assets/example_files/factor_group_ex2.json" | relative_url }})


{% include file_formats_and_locations.md %}
