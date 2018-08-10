Point group sizes: fcc, bcc, cubic, hexagonal.
```
#include <iostream>
#include "casm/crystallography/Lattice.hh"
#include "casm/symmetry/SymGroup.hh"

/// \brief Main function
int main(int argc, char** argv)
{
  CASM::SymGroup pg;
  double tol = CASM::TOL; // default tolerance = 1e-5

  pg.clear();
  CASM::Lattice::fcc().generate_point_group(pg, tol);
  std::cout << "fcc point group size: " << pg.size() << std::endl;

  pg.clear();
  CASM::Lattice::bcc().generate_point_group(pg, tol);
  std::cout << "bcc point group size: " << pg.size() << std::endl;

  pg.clear();
  CASM::Lattice::cubic().generate_point_group(pg, tol);
  std::cout << "cubic point group size: " << pg.size() << std::endl;

  pg.clear();
  CASM::Lattice::hexagonal().generate_point_group(pg, tol);
  std::cout << "hexagonal point group size: " << pg.size() << std::endl;

}

```
<details><summary markdown="span">See result</summary>

```
$ g++ -std=c++11 -O3 -DNDEBUG -I$CONDA_PREFIX/include -o lattice-pg-sec2.2 lattice-pg-sec2.2.cpp -L$CONDA_PREFIX/lib -rpath $CONDA_PREFIX/lib -lboost_system  -lcasm  && ./lattice-pg-sec2.2
fcc point group size: 48
bcc point group size: 48
cubic point group size: 48
hexagonal point group size: 24
```
</details>
<br>
