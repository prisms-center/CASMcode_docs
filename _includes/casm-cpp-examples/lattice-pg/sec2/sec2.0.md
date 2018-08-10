Generate and print the cubic lattice point group.
```
#include <iostream>
#include "casm/crystallography/Lattice.hh"
#include "casm/symmetry/SymGroup.hh"

/// \brief Main function
int main(int argc, char** argv)
{
  CASM::Lattice lat { {1., 0., 0.}, {0., 1., 0.}, {0., 0., 1.}};

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
$ g++ -std=c++11 -O3 -DNDEBUG -I$CONDA_PREFIX/include -o lattice-pg-sec2.0 lattice-pg-sec2.0.cpp -L$CONDA_PREFIX/lib -rpath $CONDA_PREFIX/lib -lboost_system  -lcasm  && ./lattice-pg-sec2.0
Lattice (as column vector matrix): 
1 0 0
0 1 0
0 0 1

Point group (Cartesian coordinates): 
48 # Cartesian representation of group containing 48 elements:

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

2  90-degree Rotation Operation about axis   0.000 1.000 0.000
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000   1.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000

3  90-degree Rotation Operation about axis   1.000 0.000 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000

4  270-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

5  270-degree Rotation Operation about axis   -0.000  1.000 -0.000
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000  -1.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000

6  270-degree Rotation Operation about axis   1.000 0.000 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000

7  120-degree Rotation Operation about axis    0.577 -0.577 -0.577
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000  -1.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000

8  120-degree Rotation Operation about axis    0.577 -0.577  0.577
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000

9  120-degree Rotation Operation about axis    0.577  0.577 -0.577
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000

10  120-degree Rotation Operation about axis   0.577 0.577 0.577
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000   1.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000

11  240-degree Rotation Operation about axis    0.577 -0.577 -0.577
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000

12  240-degree Rotation Operation about axis    0.577 -0.577  0.577
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000   1.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000

13  240-degree Rotation Operation about axis    0.577  0.577 -0.577
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000  -1.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000

14  240-degree Rotation Operation about axis   0.577 0.577 0.577
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000

15  180-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

16  180-degree Rotation Operation about axis   0.000 1.000 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

17  180-degree Rotation Operation about axis   1.000 0.000 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

18  180-degree Rotation Operation about axis    0.000  0.707 -0.707
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000

19  180-degree Rotation Operation about axis   0.000 0.707 0.707
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000

20  180-degree Rotation Operation about axis    0.707 -0.707  0.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

21  180-degree Rotation Operation about axis    0.707  0.000 -0.707
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000  -1.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000

22  180-degree Rotation Operation about axis   0.707 0.000 0.707
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000   1.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000

23  180-degree Rotation Operation about axis   0.707 0.707 0.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

24  Mirror Operation with plane normal   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

25  Mirror Operation with plane normal   0.000 1.000 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

26  Mirror Operation with plane normal   1.000 0.000 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

27  Mirror Operation with plane normal    0.000  0.707 -0.707
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000

28  Mirror Operation with plane normal   0.000 0.707 0.707
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000

29  Mirror Operation with plane normal    0.707 -0.707  0.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

30  Mirror Operation with plane normal    0.707  0.000 -0.707
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000   1.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000

31  Mirror Operation with plane normal   0.707 0.000 0.707
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000  -1.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000

32  Mirror Operation with plane normal   0.707 0.707 0.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

33  120-degree Rotoinversion Operation about axis    0.577 -0.577 -0.577
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000   1.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000

34  120-degree Rotoinversion Operation about axis    0.577 -0.577  0.577
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000

35  120-degree Rotoinversion Operation about axis    0.577  0.577 -0.577
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000

36  120-degree Rotoinversion Operation about axis   0.577 0.577 0.577
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000  -1.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000

37  240-degree Rotoinversion Operation about axis    0.577 -0.577 -0.577
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000

38  240-degree Rotoinversion Operation about axis    0.577 -0.577  0.577
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000  -1.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000

39  240-degree Rotoinversion Operation about axis    0.577  0.577 -0.577
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000   1.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000

40  240-degree Rotoinversion Operation about axis   0.577 0.577 0.577
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000

41  90-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

42  90-degree Rotoinversion Operation about axis   0.000 1.000 0.000
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000  -1.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000

43  90-degree Rotoinversion Operation about axis   1.000 0.000 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000

44  270-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

45  270-degree Rotoinversion Operation about axis   -0.000  1.000 -0.000
Symmetry Operation Matrix                            Shift 
   0.000000000   0.000000000   1.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000

46  270-degree Rotoinversion Operation about axis   1.000 0.000 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000

47  Inversion Operation
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000
```
</details>
<br>
