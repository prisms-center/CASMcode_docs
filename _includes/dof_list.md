| Name | Description | Type | Standard basis | Axis names (if different) |
|-|-|-|-|
| `"disp"`<sup>[[1]](#dof-note-1)</sup> | Atomic displacement | Site | $[d_x, d_y, d_z]$ |
| `"Cmagspin"` | Collinear magnetic spin | Site | $[m]$ |
| `"Cunitmagspin"` | Collinear magnetic spin, constrained to unit length | Site | $[m]$ |
| `"NCmagspin"` | Non-collinear magnetic spin, without spin-orbit coupling | Site |  $[s_x, s_y, s_z]$ |
| `"NCunitmagspin"` | Non-collinear magnetic spin, without spin-orbit coupling, constrained to unit length | Site | $[s_x, s_y, s_z]$ |
| `"SOmagspin"` | Non-collinear magnetic spin, with spin-orbit coupling | Site | $[s_x, s_y, s_z]$ |
| `"SOunitmagspin"` | Non-collinear magnetic spin, with spin-orbit coupling, constrained to unit length | Site | $[s_x, s_y, s_z]$ |
| `"EAstrain"`<sup>[[1]](#dof-note-1)</sup><sup>[[2]](#dof-note-2)</sup> | Euler-Almansi strain metric, $\frac{1}{2}(I-(F F^{T})^{-1})$ | Global | $[E_{xx}, E_{yy}, E_{zz}, \sqrt(2)E_{yz}, \sqrt(2)E_{xz}, \sqrt(2)E_{xy}]$ | $[e_1, e_2, e_3, e_4, e_5, e_6]$ |
| `"GLstrain"`<sup>[[1]](#dof-note-1)</sup><sup>[[2]](#dof-note-2)</sup> | Green-Lagrange strain metric, $\frac{1}{2}(C-I)$ | Global | $[E_{xx}, E_{yy}, E_{zz}, \sqrt(2)E_{yz}, \sqrt(2)E_{xz}, \sqrt(2)E_{xy}]$ | $[e_1, e_2, e_3, e_4, e_5, e_6]$ |
| `"Hstrain"`<sup>[[1]](#dof-note-1)</sup><sup>[[2]](#dof-note-2)</sup> | Hencky strain metric, $\frac{1}{2}ln(C)$ | Global | $[E_{xx}, E_{yy}, E_{zz}, \sqrt(2)E_{yz}, \sqrt(2)E_{xz}, \sqrt(2)E_{xy}]$ | $[e_1, e_2, e_3, e_4, e_5, e_6]$ |

<div>
Notes:
1. {: #dof-note-1 } When both displacements and strain are applied, displacements are applied first and then the displaced coordinates and lattice vectors are strained.
2. {: #dof-note-2 } The strain metrics, $E$, are defined in terms of the deformation gradient tensor, $F$, and Green's deformation tensor, $C$. The deformation gradient tensor relates the strained and unstrained lattices through $L^{strained} = F * L^{ideal}$, where $L$ is a column-vector matrix of the lattice vectors. The deformation matrix tensor can be decomposed, via $F = R * U$, into a rotation tensor, $R$, and stretch tensor, $U$. Green's deformation tensor, $C = F^{T}*F$, excludes rigid rotations.
</div>
{: .notice--info}
