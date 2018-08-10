Examples constructing a lattice.
```
#include <iostream>
#include "casm/crystallography/Lattice.hh"

/// \brief Main function
int main(int argc, char** argv)
{
  Eigen::Vector3d vec1 {1., 0., 0.};
  Eigen::Vector3d vec2 {0., 2., 0.};
  Eigen::Vector3d vec3 {0., 0., 3.};
  CASM::Lattice lat1 {vec1, vec2, vec3};
  std::cout << "Lattice 1 (as column vector matrix): " << std::endl;
  std::cout << lat1.lat_column_mat() << "\n" << std::endl;

  Eigen::Matrix3d M;
  M << 1., 0., 0.,
       0., 2., 0.,
       0., 0., 3.;
  CASM::Lattice lat2 {M};
  std::cout << "Lattice 2 (as column vector matrix): " << std::endl;
  std::cout << lat2.lat_column_mat() << "\n" << std::endl;

  CASM::Lattice lat3 {
    {1., 0., 0.},
    {0., 2., 0.},
    {0., 0., 3.}};
  std::cout << "Lattice 3 (as column vector matrix): " << std::endl;
  std::cout << lat3.lat_column_mat() << "\n" << std::endl;

}

```
<details><summary markdown="span">See result</summary>

```
$ g++ -std=c++11 -O3 -DNDEBUG -I$CONDA_PREFIX/include -o lattice-pg-sec1.0 lattice-pg-sec1.0.cpp -L$CONDA_PREFIX/lib -rpath $CONDA_PREFIX/lib -lboost_system  -lcasm  && ./lattice-pg-sec1.0
Lattice 1 (as column vector matrix): 
1 0 0
0 2 0
0 0 3

Lattice 2 (as column vector matrix): 
1 0 0
0 2 0
0 0 3

Lattice 3 (as column vector matrix): 
1 0 0
0 2 0
0 0 3
```
</details>
<br>
