Primitive structure symmetry is calculated when the project is initialized and can be shown with the `` `casm sym` `` command. It is a good idea to check that symmetry operations that CASM identifies match your expectations. Discrepencies may be an indication of a mistake in your specification of the lattice vectors or basis site coordinates, or a tolerance issue. The default CASM tolerance is $1^{-5}$, so it is a good idea to specify coordinates to at least that many digits.

Symmetry operation have the common notation $\\{R_\alpha\|\tau\\}$, where:
- $R_\alpha$: point group operations such as rotations, reflections, improper rotations, inversions
- $\tau$: a translation vector
- $\alpha$: a 3x3 transformation matrix

The symmetry operation $\\{R_\alpha\|\tau\\}$ transforms a Cartesian coordinate, $r$, according to:
<p align="center">
  $r^\prime = \\{R_\alpha\|\tau\\}r = \alpha r + \tau $
</p>
