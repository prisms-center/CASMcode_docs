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

Then the DoF space has dimension 6 (for 2 sites with displacements allowed in 3d), with axes labeled `"[dx[2], dy[2], dz[2], dx[4], dy[4], dz[4]]"`.

The DoF space axis labels have the format `<dof component name>[<site_index>+1]` because the current conventions in CASM are such that site indices begin with 0, but axes indices begin with 1.
</div>
{: .notice--info}

It is also possible to further restrict the DoF space by specifying a subspace via choice of a basis. Then DoF values in the DoF space can be converted between representations in the [standard basis], the user-specified [prim basis], and the DoF space basis using:

$$
\begin{align*}
v^{standard} &= B^{prim} * v^{prim} \\
v^{prim} &= B^{dofspace} * v^{dofspace}
\end{align*}
$$

where:
- $v^{standard}$ are DoF values represented in the [standard basis] (`shape=(standard_dim,)`)
- $v^{prim}$ are DoF values in the user-specified [prim basis] (`shape=(dim,)`)
- $v^{dofspace}$ are DoF values in the DoF space basis (`shape=(dofspace_dim,)`)
- $B^{prim}$ is the user-specified [prim basis] (`shape=(standard_dim, dim)`)
- $B^{dofspace}$ is the DoF space basis (`shape=(dim, dofspace_dim)`)

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

To sample crystal states in a DoF space, an efficient way to proceed is to find the "irreducible wedge" (the portion of the DoF space that falls between high symmetry directions and fills the entire DoF space under application of the relevant symmetry group, `g`) and enumerate states within the irreducible wedge.

CASM can perform a DoF space symmetry analysis to identify the irreducible subspaces (the subspaces of the full DoF space that are unchanged under transformation by `g`). Once those are found, CASM constructs "symmetry-adapted axes" (a DoF space basis with axes aligned with the irreducible subspaces), identify the high symmetry directions, and construct the irreducible wedge.

The irreducible wedge itself is formed by a combination of one or more "subwedges", each of which spans the DoF space basis, but by itself may not fill the entire DoF space under application of `g`. The "subwedges" are in turn constructed from a symmetrically unique portion of an irreducible subspace (an "irrep wedge").

**Note:** A symmetry analysis of a displacement DoF space that includes all sites in a supercell will also find rigid translations so that they can be removed.
{: .notice--info}

#### Project files

This format is used for [`dof_space_<dof_type>.json`] files. A DoF space symmetry analysis can be performed using `casm sym --dof-space-analysis`.


### Examples

Example DoF Space files:
1. Displacement DoF Space, selecting 2 of 4 total configuration sites: [[dof_space_disp_ex1.json]]({{ "/assets/example_files/dof_space_disp_ex1.json" | relative_url }})
2. Displacement DoF Space, including all 4 total configuration sites, and identifying rigid translations ("homogeneous modes"): [[dof_space_disp_ex2.json]]({{ "/assets/example_files/dof_space_disp_ex2.json" | relative_url }})

[standard basis]:  {{ "/formats/casm/crystallography/BasicStructure#dof-list" |  relative_url }}
[prim basis]:  {{ "/formats/casm/crystallography/BasicStructure#user-specified-dof-basis" |  relative_url }}

{% include file_formats_and_locations.md %}
