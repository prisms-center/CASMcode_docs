---
title: "DoF Space"
permalink: /formats/casm/enumerator/DoFSpace/
---

### Description

A degrees of freedom (DoF) space is a subset of the crystal states allowed by a [Prim].


#### Defining a DoF space

A DoF space is specified by selecting a DoF type (for example `"disp"`, `"GLstrain"`, or `"occ"`), and, for site DoF, a supercell and set of sites whose DoF are included in the DoF space.

<div>
**Example:**

Consider a configuration with 4 sites, each with displacement DoF allowed. Let 2 sites (with site indices 0 and 2) be fixed at zero displacement, and define a displacement DoF space consisting of the other 2 sites (with site indices 1 and 3) which are allowed to vary completely.

Then the DoF space has dimension 6 (for 2 sites with displacements allowed in 3d), with axes labeled `["dx[2]", "dy[2]", "dz[2]", "dx[4]", "dy[4]", "dz[4]"]`.

The DoF space axis labels have the format `<prim_basis_axis_name>[<site_index>+1]` because the current conventions in CASM are such that site indices begin with 0, but axes indices begin with 1.
</div>
{: .notice--info}

It is also possible to further restrict the DoF space by specifying a subspace via choice of a basis. Then DoF values in the DoF space can be converted between representations in the [standard basis], the user-specified [prim basis], and the DoF space basis using:

$$
\begin{align*}
v^{standard} &= Q^{prim} * v^{prim} \\
v^{prim} &= Q^{dofspace} * v^{dofspace}
\end{align*}
$$

where:
- $v^{standard}$ are DoF values represented in the [standard basis] (`shape=(standard_dim,)`)
- $v^{prim}$ are DoF values in the user-specified [prim basis] (`shape=(prim_dim,)`)
- $v^{dofspace}$ are DoF values in the DoF space basis (`shape=(dofspace_dim,)`)
- $Q^{prim}$ is a matrix constructed from the user-specified [prim basis] for all DoF included in the DoF space (`shape=(standard_dim, prim_dim)`)
- $Q^{dofspace}$ is the DoF space basis (`shape=(prim_dim, dofspace_dim)`)
- `standard_dim` is the sum of the [standard basis] dimension for all DoF included in the DoF space
- `prim_dim` is the sum of the user-specified [prim basis] dimension for all DoF included in the DoF space
- `dofspace_dim` is the subspace dimension specified by choice of $Q^{dofspace}$


<div>
**Example:** Given the previous example, the DoF space can be further limited to only displacements along x on the two selected sites with the choice:

$$
\begin{align*}
B^{dofspace} = \left[ \begin{array}{cc}
      1 & 0 \\
      0 & 0 \\
      0 & 0 \\
      0 & 1 \\
      0 & 0 \\
      0 & 0
    \end{array} \right]
\end{align*}
$$
</div>
{: .notice--info}


#### DoF space symmetry analysis

To sample crystal states in a DoF space, an efficient way to proceed is to find the "irreducible wedge" (the portion of the DoF space that falls between high symmetry directions and fills the entire DoF space under application of the relevant symmetry group, $g$) and enumerate states within the irreducible wedge.

CASM can perform a DoF space symmetry analysis to identify the irreducible subspaces (the subspaces of the full DoF space that are unchanged under transformation by $g$). Once those are found, CASM constructs "symmetry-adapted axes" (a DoF space basis with axes aligned with the irreducible subspaces), identify the high symmetry directions, and construct the irreducible wedge.

The irreducible wedge itself is formed by a combination of one or more "subwedges", each of which spans the DoF space basis, but by itself may not fill the entire DoF space under application of $g$. The "subwedges" are in turn constructed from a symmetrically unique portion of an irreducible subspace (an "irrep wedge").

**Note:** A symmetry analysis of a displacement DoF space that includes all sites in a supercell will also find rigid translations so that they can be removed.
{: .notice--info}

**Note:** For more details, see J. C. Thomas, A. Van der Ven, *J. Mech. Phys. Solids* **107** 76–95 (2017) doi:[10.1016/j.jmps.2017.06.009](http://dx.doi.org/10.1016/j.jmps.2017.06.009).
{: .notice--info}


#### Project files

This format is used for [`dof_space_<dof_type>.json`] files. A DoF space symmetry analysis can be performed using `casm sym --dof-space-analysis`.


### JSON Attribute List

Configuration attributes:

| Name | Description | Format |
|-|-|-|
| [`axis_dof_component`](#axis-dof-component) | DoF component index, in the [prim basis], specified by each element of $v^{prim}$ | null or array of int |
| [`axis_site_index`](#axis-site-index) | Site index of the DoF specified by each element of $v^{prim}$ | null or array of int |
| [`basis`](#basis) | DoF subspace basis $(Q^{dofspace})^{\top}$ | 2d array of number |
| [`dof`](#dof) | DoF type | string |
| [`glossary`](#glossary) | DoF space axes names | array of string |
| [`identifier`](#identifier) | DoF space identifier | string |
| [`irreducible_representations`](#irreducible-representations) | Irreducible space decomposition results | [Irrep Decomposition] |
| [`irreducible_wedge`](#irreducible-wedge) | Irreducible wedge of the DoF space | dict |
| [`sites`](#sites) | Sites included in the DoF space | null or array of int |
| [`state`](#state) | Configuration state | null or [Configuration state] |
| [`symmetry_representation`](#symmetry-representation) | Symmetry group matrix representation | 3d array of number |
| [`transformation_matrix_to_supercell`](#transformation-matrix-to-supercell) | Transformation matrix from prim to supercell lattice vectors | null or 2d array of int |

---

Irrep Decomposition attributes:

| Name | Description | Format |
|-|-|-|
| [`adapted_axes`](#adapted-axes) | Symmetry adapted axes | dict |
| [`irreducible_wedge`](#irreducible-wedge) | Irreducible wedges of the irreducible spaces | dict |
| [`irrep_axes`](#irrep-axes) | Axes of each irreducible space | dict |
| [`subgroup_invariant_directions`](#subgroup-invariant-directions) | High-symmetry directions of each irreducible space | dict |
| [`symop_matrices`](#symop-matrices) | Symmetry group matrix representation for reach irreducible space | dict |


### JSON Attributes Description

#### DoF Space JSON object

- {: #axis-dof-component } `axis_dof_component`: null or array of int, (`shape=(standard_dim,)`)

  For a site DoF space, `axis_dof_component[i]` is the index in the user-specified [prim basis] of the DoF specified by $v^{prim}_{i}$.

  For a global DoF space, it is null. The user-specified [prim basis] is always used for a global DoF space.

  <div>
  **Example:** A displacement DoF space of 2 sites, where the user-specified [prim basis] is 2d with axes `["d1", "d2"]`

      "axis_dof_component": [0, 1, 0, 1]

  </div>
  {: .notice--info }

  <div>
  **Example:** A displacement DoF space of 2 sites, using the [standard basis] with axes `["dx", "dy", "dz"]`

      "axis_dof_component": [0, 1, 2, 0, 1, 2]

  </div>
  {: .notice--info }

- {: #axis-site-index } `axis_site_index`: null or array of int, (`shape=(standard_dim,)`)

  For a site DoF space, `axis_site_index[i]` is the [site index] of the DoF specified by $v^{prim}_{i}$.

  For a global DoF space, it is null.

  <div>
  **Example:** A displacement DoF space of 2 sites, with site indices `[1, 3]`, where the user-specified [prim basis] is 2d with axes `["d1", "d2"]`

      "axis_site_index": [1, 1, 3, 3]

  </div>
  {: .notice--info }

  <div>
  **Example:** A displacement DoF space of 2 sites, with site indices `[1, 3]`, using the [standard basis] with axes `["dx", "dy", "dz"]`

      "axis_site_index": [1, 1, 1, 3, 3, 3]

  </div>
  {: .notice--info }

- {: #basis } `basis`: 2d array of number, `shape=(dofspace_dim, prim_dim)`

  The DoF space basis, printed as the transpose, $(Q^{dofspace})^{\top}$, so that it is an array of axes in the full DoF space.

- {: #dof } `dof`: string

  The name of the DoF type described by this DoF space.

- {: #glossary } `glossary`: array of string

  Strings describing each component of $v^{prim}$.

  The DoF space axis labels listed in `glossary` have the format `<prim_basis_axis_name>[<site_index>+1]` because the current conventions in CASM are such that site indices begin with 0, but axes indices begin with 1.

  <div>
  **Example:** A displacement DoF space of 2 sites, where the user-specified [prim basis] is 2d with axes `["d1", "d2"]`

      "glossary": ["d1[2]", "d2[2]", "d1[4]", "d2[4]"]

  </div>
  {: .notice--info }

- {: #identifier } `identifier`: string

  A string to help users identify the DoF space, particularly in situations where many DoF spaces are considered in a batch operation. Typically it is a supercell name, configuration name, or configuration name and description of selected sites.

- {: #irreducible-representations } `irreducible_representations`: [Irrep Decomposition]

  Irreducible space decomposition results

- {: #irreducible-wedge }`irreducible_wedge`: dict

  For each "subwedge" of the total irreducible wedge, an array (of size `dofspace_dim`) of axes (of size `prim_dim`) defining the edges of the subwedge. The combination of all subwedges is the total irreducible wedge.

  <div>
  **Example:**

      "irreducible_wedge" : {
        "subwedge_axes_1" : [ // size = dofspace_dim
          [... subwedge 1, axis 1 ...],  // size = prim_dim
          [... subwedge 1, axis 2 ...],
          ...
        ],
        "subwedge_axes_2" : [[... array of subwedge axes ...]],
        "subwedge_axes_3" : [[... array of subwedge axes ...]],
        ...
      }

  </div>
  {: .notice--info }

-  {: #sites } `sites`: null or array of int

  For a site DoF, an array of [site index] of the sites with DoF included in the DoF space.

  For a global DoF space, it is null.

- {: #state } `state`:  null or [Configuration state]

  The [Configuration state] specifies a [Configuration] and set of selected sites.

  The group of symmetry operations that (i) leaves the DoF values of the background configuration invariant, and (ii) does not cause any permutation between the set of selected and unselected sites is the group, $g$, used for the DoF space symmetry analysis. For a global DoF space, all sites will be selected.

- {: #symmetry-representation} `symmetry_representation`: 3d array of number (`shape=(g_size, prim_dim, prim_dim)`)

  The element `symmetry_representation[i]` is a matrix representation, $M_{i}$, for the symmetry operation $g_{i}$ in group $g$ of size `g_size`, which transforms $v^{prim}$ according to $v_{after}^{prim} = M_{i} * v_{before}^{prim}$.

- {: #transformation-matrix-to-supercell } `transformation_matrix_to_supercell`: null or 2d array of int (`shape=(3,3)`)

  For a site DoF space, the matrix that transforms the [prim] lattice vectors into the supercell lattice vectors. Defined as in [Configuration]({{ "/formats/casm/clex/Configuration#transformation-matrix-to-supercell" | relative_url }}).

  For a global DoF space, it is null.


#### Irrep Decomposition JSON object

Results of an irreducible space decomposition.

- {: #adapted-axes } `adapted_axes`: dict (`size=dofspace_dim`)

  The symmetry adapted axes, labeled `q1`, `q2`, etc. are axes (of size `prim_dim` and represented in terms of $Q^{prim}$ column axes) aligned along high-symmetry directions in the irreducible spaces. Combined as a basis set, they form the columns of a possible choice of $Q^{dofspace}$ which spans the same DoF space as [`basis`](#basis).

  <div>
  **Example:** Symmetry adapted axes for a subspace (`dofspace_dim=3`) of the full strain DoF space (`prim_dim=6`) using the Hency strain metric (`Hstrain`) for a FCC [prim] with given basis.

      "basis" : [
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
      ]

      "adapted_axes" : {
        "q1" : [ 0.577350269190, 0.577350269190, 0.577350269190, 0.000000000000, 0.000000000000, 0.000000000000 ],
        "q2" : [ -0.408248290464, -0.408248290464, 0.816496580928, 0.000000000000, 0.000000000000, -0.000000000000 ],
        "q3" : [ 0.707106781187, -0.707106781187, -0.000000000000, -0.000000000000, -0.000000000000, 0.000000000000 ]
      }
  </div>
  {: .notice--info }

- {: #irreducible-wedge } `irreducible_wedge`: dict

  Irreducible wedges of the irreducible spaces. Irreducible wedge axes are vectors represented in terms of the adapted axes spanning each irreducible space (as ordered by [`irrep_axes`](#irrep-axes).

  <div>
  **Example:** Irreducible wedges for the irreducible spaces of the full strain DoF space (`prim_dim=6`) using the Hencky strain metric (`Hstrain`) for a FCC [prim].

      "irreducible_wedge" : {
        "irrep_1_1" : [
          [ 1.000000000000 ]
        ],
        "irrep_2_1" : [
          [ -0.500000000000, 0.866025403784 ],
          [ -1.000000000000, 0.000000000000 ]
        ],
        "irrep_3_1" : [
          [ 1.000000000000, 0.000000000000, 0.000000000000 ],
          [ 0.577350269190, 0.577350269190, 0.577350269190 ],
          [ 0.577350269190, 0.577350269190, -0.577350269190 ]
        ]
      }

  </div>
  {: .notice--info }

- {: #irrep-axes } `irrep_axes`: dict

  The names of the axes (defined in `adapted_axes`) of each irreducible space. Irreducible spaces names follow the convention `irrep_<i>_<j>`, where the `i` index comes from sorting irreps according to properties including their dimension and character vectors, and `j` is a sequential index to differentiate irreps with the same character vectors.

  <div>
  **Example:**

      "irrep_axes" : {
        "irrep_1_1" : [ "q1" ],
        "irrep_2_1" : [ "q2", "q3" ],
        "irrep_3_1" : [ "q4", "q5", "q6" ]
      }

  </div>
  {: .notice--info }

- {: #subgroup-invariant-directions } `subgroup_invariant_directions`: dict

  The orbits of the high-symmetry directions of each irreducible space. The high symmetry directions are vectors represented in terms of the adapted axes spanning each irreducible space (as ordered by [`irrep_axes`](#irrep-axes).

  <div>
  **Example:**

      "subgroup_invariant_directions" : {
        "irrep_1_1" : {
          "direction_orbit_1" : [
            [ 1.000000000000 ]
          ],
          "direction_orbit_2" : [
            [ -1.000000000000 ]
          ]
        },
        "irrep_2_1" : {
          "direction_orbit_1" : [
            [ -0.500000000000, 0.866025403784 ],
            [ -0.500000000000, -0.866025403784 ],
            [ 1.000000000000, -0.000000000000 ]
          ],
          "direction_orbit_2" : ...
        },
        "irrep_3_1" : ...
      }

  </div>
  {: .notice--info }

- {: #symop-matrices } `symop_matrices`: dict

  Symmetry group matrix representation for transforming vectors in each irreducible space.

  <div>
  **Example:**

      "symop_matrices" : {
        "irrep_1_1" : {
          "op_01": [[... matrix rep ...]],
          "op_02": [[... matrix rep ...]],
          ...
        },
        "irrep_2_1" : {
          "op_01": [[... matrix rep ...]],
          "op_02": [[... matrix rep ...]],
          ...
        },
        "irrep_3_1" : {
          "op_01": [[... matrix rep ...]],
          "op_02": [[... matrix rep ...]],
          ...
        }
      }

  </div>
  {: .notice--info }


### Examples

Example DoF Space files:
1. Strain DoF space, using the Hencky strain metric, of a system with an FCC [prim]: [[dof_space_Hstrain_ex1.json]]({{ "/assets/example_files/dof_space_Hstrain_ex1.json" | relative_url }})
2. Displacement DoF space, selecting 2 of 4 total configuration sites in the L1<sub>2</sub> ordering of a system with an FCC [prim]: [[dof_space_disp_ex1.json]]({{ "/assets/example_files/dof_space_disp_ex1.json" | relative_url }})
3. Displacement DoF space, including all 4 total configuration sites, and identifying rigid translations ("homogeneous modes"), in the L1<sub>2</sub> ordering of a system with an FCC [prim]: [[dof_space_disp_ex2.json]]({{ "/assets/example_files/dof_space_disp_ex2.json" | relative_url }})

[standard basis]:  {{ "/formats/casm/crystallography/BasicStructure#dof-list" |  relative_url }}
[prim basis]:  {{ "/formats/casm/crystallography/BasicStructure#user-specified-dof-basis" |  relative_url }}
[site index]: {{ "/formats/casm/clex/Configuration#occ" |  relative_url }}

{% include file_formats_and_locations.md %}
