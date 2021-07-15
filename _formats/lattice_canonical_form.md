---
title: "Lattice Canonical Form"
permalink: /formats/lattice_canonical_form/
toc: false
---

CASM determines the canonical form of a lattice with respect to a point group, $g$, by (i) finding all equivalent spatial orientations of the Niggli cell of the lattice, (ii) applying all operations in $g$ to generate all symmetrically equivalent Niggli cell lattice vectors, and (iii) finding the lattice vectors (represented as a column vector matrix) that have the most standard orientation according to the following criteria:
  - bisymmetric matrices are always more standard than symmetric matrices
  - symmetric matrices are always more standard than non-symmetric matrices
  - matrices with more positive values are preferred
  - matrices with large values on the diagonal are preferred
  - matrices with small off-diagonal values are preferred
  - upper triangular matrices are preferred

For lattices without any basis, the appropriate point group is the lattice point group.

For supercells of a [prim], the appropriate point group is the crystal point group.

[prim]: {{ "/formats/casm/crystallography/BasicStructure" |  relative_url }}
