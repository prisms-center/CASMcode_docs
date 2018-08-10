Generate and print the tetragonal lattice point group.
```
#include <iostream>
#include "casm/crystallography/Lattice.hh"
#include "casm/symmetry/SymGroup.hh"

/// \brief Main function
int main(int argc, char** argv)
{
  CASM::Lattice lat { {1., 0., 0.}, {0., 1., 0.}, {0., 0., 2.}};

  std::cout << "Lattice (as column vector matrix): " << std::endl;
  std::cout << lat.lat_column_mat() << "\n" << std::endl;

  CASM::SymGroup pg;
  double tol = CASM::TOL; // default tolerance = 1e-5
  lat.generate_point_group(pg, tol);

  std::cout << "Point group (Cartesian coordinates): \n";
  pg.print(std::cout, CASM::CART);

}

```
<details><summary markdown="span">See result</summary>

```
$ g++ -std=c++11 -O3 -DNDEBUG -I$CONDA_PREFIX/include -o lattice-pg-sec2.1 lattice-pg-sec2.1.cpp -L$CONDA_PREFIX/lib -rpath $CONDA_PREFIX/lib -lboost_system  -lcasm  && ./lattice-pg-sec2.1
Lattice (as column vector matrix): 
1 0 0
0 1 0
0 0 2

Point group (Cartesian coordinates): 
16 # Cartesian representation of group containing 16 elements:

0  Identity Operation
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

1  90-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

2  270-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

3  180-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

4  180-degree Rotation Operation about axis   0.000 1.000 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

5  180-degree Rotation Operation about axis   1.000 0.000 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

6  180-degree Rotation Operation about axis    0.707 -0.707  0.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

7  180-degree Rotation Operation about axis   0.707 0.707 0.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

8  Mirror Operation with plane normal   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

9  Mirror Operation with plane normal   0.000 1.000 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

10  Mirror Operation with plane normal   1.000 0.000 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

11  Mirror Operation with plane normal    0.707 -0.707  0.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

12  Mirror Operation with plane normal   0.707 0.707 0.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

13  90-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

14  270-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

15  Inversion Operation
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000
```
</details>
<br>
