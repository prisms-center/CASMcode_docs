| Name | Description | Type | Variable descriptions | Variable names (if different) |
|-|-|-|-|
| `"cost"` | Cost function value | Global | $[C]$ | |
| `"disp"`<sup>[[1]](#prop-note-1)</sup> | Atomic displacement | Site | $[d_x, d_y, d_z]$ | |
| `"energy"` | Energy | Global | $[E]$ | |
| `"force"` | Force | Site | $[f_x, f_y, f_z]$ | |
| `"Cmagspin"` | Collinear magnetic spin | Site | $[m]$ | |
| `"Cunitmagspin"` | Collinear magnetic spin, constrained to unit length | Site | $[m]$ | |
| `"NCmagspin"` | Non-collinear magnetic spin, without spin-orbit coupling | Site |  $[s_x, s_y, s_z]$ | |
| `"NCunitmagspin"` | Non-collinear magnetic spin, without spin-orbit coupling, constrained to unit length | Site | $[s_x, s_y, s_z]$ | |
| `"SOmagspin"` | Non-collinear magnetic spin, with spin-orbit coupling | Site | $[s_x, s_y, s_z]$ | |
| `"SOunitmagspin"` | Non-collinear magnetic spin, with spin-orbit coupling, constrained to unit length | Site | $[s_x, s_y, s_z]$ | |
| `"selectivedynamics"`<sup>[[2]](#prop-note-2)</sup> | Selective dynamics tag | Site | ["aflag", "bflag", "cflag"] | |
| `"Bstrain"`<sup>[[1]](#prop-note-1)</sup><sup>[[3]](#prop-note-3)</sup> | Biot strain metric, $(U-I)$ | Global | $[E_{xx}, E_{yy}, E_{zz}, \sqrt(2)E_{xz}, \sqrt(2)E_{yz}, \sqrt(2)E_{xy}]$ | $[e_1, e_2, e_3, e_4, e_5, e_6]$ |
| `"EAstrain"`<sup>[[1]](#prop-note-1)</sup><sup>[[3]](#prop-note-3)</sup>  | Euler-Almansi strain metric, $\frac{1}{2}(I-(F F^{T})^{-1})$ | Global | $[E_{xx}, E_{yy}, E_{zz}, \sqrt(2)E_{xz}, \sqrt(2)E_{yz}, \sqrt(2)E_{xy}]$ | $[e_1, e_2, e_3, e_4, e_5, e_6]$ |
| `"GLstrain"`<sup>[[1]](#prop-note-1)</sup><sup>[[3]](#prop-note-3)</sup> | Green-Lagrange strain metric, $\frac{1}{2}(C-I)$ | Global | $[E_{xx}, E_{yy}, E_{zz}, \sqrt(2)E_{xz}, \sqrt(2)E_{yz}, \sqrt(2)E_{xy}]$ | $[e_1, e_2, e_3, e_4, e_5, e_6]$ |
| `"Hstrain"`<sup>[[1]](#prop-note-1)</sup><sup>[[3]](#prop-note-3)</sup> | Hencky strain metric, $\frac{1}{2}ln(C)$ | Global | $[E_{xx}, E_{yy}, E_{zz}, \sqrt(2)E_{xz}, \sqrt(2)E_{yz}, \sqrt(2)E_{xy}]$ | $[e_1, e_2, e_3, e_4, e_5, e_6]$ |
| `"Ustrain"`<sup>[[1]](#prop-note-1)</sup><sup>[[3]](#prop-note-3)</sup> | Right stretch tensor, $U$ | Global | $[E_{xx}, E_{yy}, E_{zz}, \sqrt(2)E_{xz}, \sqrt(2)E_{yz}, \sqrt(2)E_{xy}]$ | $[e_1, e_2, e_3, e_4, e_5, e_6]$ |

<div>
Notes:
1. {: #prop-note-1 } When both displacements and strain are applied, displacements are applied first and then the displaced coordinates and lattice vectors are strained.
2. {: #prop-note-2 } The `"selectivedynamics"` tag should be given a value of `1` to allow displacements along a given lattice vector (corresponding to `T` in a VASP POSCAR) and `0` to prevent them (`F` in a VASP POSCAR). The current implementation may be used with either (i) volume 1 configurations only, or (ii) restricted to the values `[1., 1., 1.]` or `[0., 0., 0.]`. Using `"selectivedynamics"` with mixed values (ex: `[1., 0., 0.]` and volume >1 configurations is not currently supported and will likely give invalid results because they will be applied to the supercell lattice vectors.
3. {: #prop-note-3 } The strain metrics, $E$, are defined in terms of the deformation gradient tensor, $F$, and Green's deformation tensor, $C$. The deformation gradient tensor relates the strained and unstrained lattices through $L^{strained} = F * L^{ideal}$, where $L$ is a column-vector matrix of the lattice vectors. The deformation matrix tensor can be decomposed, via $F = R * U$, into a rotation tensor, $R$, and stretch tensor, $U$. Green's deformation tensor, $C = F^{T}*F$, excludes rigid rotations.
</div>
{: .notice--info}
