Other lattice properties.
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

  std::cout << "Angles: " << lat.angle(0) << " " << lat.angle(1) << " " << lat.angle(2) << std::endl;
  std::cout << "Lengths: " << lat.length(0) << " " << lat.length(1) << " " << lat.length(2) << std::endl;
  std::cout << "Volume: " << lat.vol() << "\n" << std::endl;

  std::cout << "Reciprocal lattice (as column vector matrix): " << std::endl;
  std::cout << lat.get_reciprocal().lat_column_mat() << "\n" << std::endl;

  std::cout << "2x2x2 Supercell (as column vector matrix): " << std::endl;
  Eigen::Matrix3i T;
  T << 2, 0, 0,
       0, 2, 0,
       0, 0, 2;
  CASM::Lattice super_lat = make_supercell(lat, T);
  std::cout << super_lat.get_reciprocal().lat_column_mat() << "\n" << std::endl;

}

```
<details><summary markdown="span">See result</summary>

```
$ g++ -std=c++11 -O3 -DNDEBUG -I$CONDA_PREFIX/include -o lattice-pg-sec1.2 lattice-pg-sec1.2.cpp -L$CONDA_PREFIX/lib -rpath $CONDA_PREFIX/lib -lboost_system  -lcasm  && ./lattice-pg-sec1.2
Angles: 90 90 90
Lengths: 1 2 3
Volume: 6

Reciprocal lattice (as column vector matrix): 
6.28319       0       0
      0 3.14159       0
      0       0  2.0944

2x2x2 Supercell (as column vector matrix): 
3.14159       0       0
      0  1.5708       0
      0       0  1.0472
```
</details>
<br>
