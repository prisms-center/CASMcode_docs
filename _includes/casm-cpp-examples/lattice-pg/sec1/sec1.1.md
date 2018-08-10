Example constructing a lattice and checking its lattice vectors.
```
#include <iostream>
#include "casm/crystallography/Lattice.hh"

/// \brief Main function
int main(int argc, char** argv)
{
  Eigen::Vector3d vec1 {1., 0., 0.};
  Eigen::Vector3d vec2 {0., 2., 0.};
  Eigen::Vector3d vec3 {0., 0., 3.};

  CASM::Lattice lat {vec1, vec2, vec3};

  std::cout << "A lattice (as column vector matrix): " << std::endl;
  std::cout << lat.lat_column_mat() << "\n" << std::endl;

  std::cout << "The first lattice vector: " << lat[0].transpose() << "\n" << std::endl;

  std::cout << "Lattice vectors as column matrix: \n" << lat.lat_column_mat() << "\n" << std::endl;

  std::cout << "Get lattice vectors as a std::tuple" << std::endl;
  Eigen::Vector3d a, b, c;
  std::tie(a, b, c) = lat.vectors();

  std::cout << "a: " << a.transpose() << std::endl;
  std::cout << "b: " << b.transpose() << std::endl;
  std::cout << "c: " << c.transpose() << std::endl;

}

```
<details><summary markdown="span">See result</summary>

```
$ g++ -std=c++11 -O3 -DNDEBUG -I$CONDA_PREFIX/include -o lattice-pg-sec1.1 lattice-pg-sec1.1.cpp -L$CONDA_PREFIX/lib -rpath $CONDA_PREFIX/lib -lboost_system  -lcasm  && ./lattice-pg-sec1.1
A lattice (as column vector matrix): 
1 0 0
0 2 0
0 0 3

The first lattice vector: 1 0 0

Lattice vectors as column matrix: 
1 0 0
0 2 0
0 0 3

Get lattice vectors as a std::tuple
a: 1 0 0
b: 0 2 0
c: 0 0 3
```
</details>
<br>
