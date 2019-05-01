{% include tutorials/init/sec_sym/sec_sym.0-desc.md %}
```
$ casm sym -h
$ casm sym
$ casm sym --factor-group
$ casm sym --lattice-point-group
$ casm sym --crystal-point-group
```
<details><summary markdown="span">See result</summary>

```
$ casm sym -h

'casm sym' usage:
  -h [ --help ]          Print help message
  --desc                 Print extended usage description
  --coord <type> (=frac) Type of coordinate system to use. Use 'frac' for 
                         fractional (default) or 'cart' for Cartesian.
  --lattice-point-group  Pretty print lattice point group
  --factor-group         Pretty print factor group
  --crystal-point-group  Pretty print crystal point group

$ casm sym
Generating lattice point group. 

  Lattice point group size: 24
  Lattice point group is: D6h

Generating factor group. 

  Factor group size: 24
  Crystal point group is: D6h

$ casm sym --factor-group
Generating lattice point group. 

  Lattice point group size: 24
  Lattice point group is: D6h

Generating factor group. 

  Factor group size: 24
  Crystal point group is: D6h

***************************

Factor group:


24 # Direct representation of group containing 24 elements:

0  Identity Operation
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

1  60-degree Screw Operation along axis   0.000 0.000 1.000
 Screw Vector:   0.000 0.000 0.500
Symmetry Operation Matrix                            Shift 
   1.000000000  -1.000000000   0.000000000           0.666666700
   1.000000000   0.000000000   0.000000000           0.333333300
   0.000000000   0.000000000   1.000000000           0.500000000

2  300-degree Screw Operation along axis   0.000 0.000 1.000
 Screw Vector:   0.000 0.000 0.500
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.666666600
  -1.000000000   1.000000000   0.000000000           0.333333300
   0.000000000   0.000000000   1.000000000           0.500000000

3  120-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

4  240-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

5  180-degree Rotation Operation about axis   -0.000 -1.000  0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000  -0.000000000   0.000000000           0.666666700
  -1.000000000   1.000000000   0.000000000           0.333333300
   0.000000000   0.000000000  -1.000000000           0.500000000

6  180-degree Screw Operation along axis   1.000 0.000 0.000
 Screw Vector:   0.500 0.000 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000  -1.000000000   0.000000000           0.666666700
   0.000000000  -1.000000000   0.000000000           0.333333400
   0.000000000   0.000000000  -1.000000000           0.500000000

7  180-degree Screw Operation along axis   0.707 0.707 0.000
 Screw Vector:   0.500 0.500 0.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.666666600
   1.000000000   0.000000000   0.000000000           0.333333300
   0.000000000   0.000000000  -1.000000000           0.500000000

8  180-degree Screw Operation along axis   0.000 0.000 1.000
 Screw Vector:   0.000 0.000 0.500
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.666666700
   0.000000000  -1.000000000   0.000000000           0.333333400
   0.000000000   0.000000000   1.000000000           0.500000000

9  180-degree Rotation Operation about axis    0.707 -0.707  0.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

10  180-degree Rotation Operation about axis   0.447 0.894 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

11  180-degree Rotation Operation about axis   0.894 0.447 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

12  Mirror Operation with plane normal   -0.000 -1.000  0.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

13  Mirror Operation with plane normal   1.000 0.000 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

14  Mirror Operation with plane normal   0.707 0.707 0.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

15  Mirror Operation with plane normal   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

16  Glide Operation with plane normal    0.707 -0.707  0.000
Glide Vector:   0.500 0.500 0.500
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.666666600
   1.000000000   0.000000000   0.000000000           0.333333300
   0.000000000   0.000000000   1.000000000           0.500000000

17  Glide Operation with plane normal   0.447 0.894 0.000
Glide Vector:   0.500 0.000 0.500
Symmetry Operation Matrix                            Shift 
   1.000000000  -1.000000000   0.000000000           0.666666700
   0.000000000  -1.000000000   0.000000000           0.333333400
   0.000000000   0.000000000   1.000000000           0.500000000

18  Glide Operation with plane normal   0.894 0.447 0.000
Glide Vector:   -0.000 -0.000  0.500
Symmetry Operation Matrix                            Shift 
  -1.000000000  -0.000000000   0.000000000           0.666666700
  -1.000000000   1.000000000   0.000000000           0.333333300
   0.000000000   0.000000000   1.000000000           0.500000000

19  120-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.666666600
  -1.000000000   1.000000000   0.000000000           0.333333300
   0.000000000   0.000000000  -1.000000000           0.500000000

20  240-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   1.000000000  -1.000000000   0.000000000           0.666666700
   1.000000000   0.000000000   0.000000000           0.333333300
   0.000000000   0.000000000  -1.000000000           0.500000000

21  60-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

22  300-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

23  Inversion Operation
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.666666700
   0.000000000  -1.000000000   0.000000000           0.333333400
   0.000000000   0.000000000  -1.000000000           0.500000000


$ casm sym --lattice-point-group
Generating lattice point group. 

  Lattice point group size: 24
  Lattice point group is: D6h

Generating factor group. 

  Factor group size: 24
  Crystal point group is: D6h

***************************

Lattice point group:


24 # Direct representation of group containing 24 elements:

0  Identity Operation
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

1  60-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   1.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

2  300-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

3  120-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

4  240-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

5  180-degree Rotation Operation about axis   -0.000 -1.000  0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000  -0.000000000   0.000000000           0.000000000
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

6  180-degree Rotation Operation about axis   1.000 0.000 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

7  180-degree Rotation Operation about axis   0.707 0.707 0.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

8  180-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

9  180-degree Rotation Operation about axis    0.707 -0.707  0.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

10  180-degree Rotation Operation about axis   0.447 0.894 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

11  180-degree Rotation Operation about axis   0.894 0.447 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

12  Mirror Operation with plane normal   -0.000 -1.000  0.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

13  Mirror Operation with plane normal   1.000 0.000 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

14  Mirror Operation with plane normal   0.707 0.707 0.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

15  Mirror Operation with plane normal   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

16  Mirror Operation with plane normal    0.707 -0.707  0.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

17  Mirror Operation with plane normal   0.447 0.894 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

18  Mirror Operation with plane normal   0.894 0.447 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000  -0.000000000   0.000000000           0.000000000
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

19  120-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

20  240-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   1.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

21  60-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

22  300-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

23  Inversion Operation
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000


$ casm sym --crystal-point-group
Generating lattice point group. 

  Lattice point group size: 24
  Lattice point group is: D6h

Generating factor group. 

  Factor group size: 24
  Crystal point group is: D6h

***************************

Crystal point group:


24 # Direct representation of group containing 24 elements:

0  Identity Operation
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

1  60-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   1.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

2  300-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

3  120-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

4  240-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

5  180-degree Rotation Operation about axis   -0.000 -1.000  0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000  -0.000000000   0.000000000           0.000000000
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

6  180-degree Rotation Operation about axis   1.000 0.000 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

7  180-degree Rotation Operation about axis   0.707 0.707 0.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

8  180-degree Rotation Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

9  180-degree Rotation Operation about axis    0.707 -0.707  0.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

10  180-degree Rotation Operation about axis   0.447 0.894 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

11  180-degree Rotation Operation about axis   0.894 0.447 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

12  Mirror Operation with plane normal   -0.000 -1.000  0.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

13  Mirror Operation with plane normal   1.000 0.000 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

14  Mirror Operation with plane normal   0.707 0.707 0.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

15  Mirror Operation with plane normal   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

16  Mirror Operation with plane normal    0.707 -0.707  0.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

17  Mirror Operation with plane normal   0.447 0.894 0.000
Symmetry Operation Matrix                            Shift 
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

18  Mirror Operation with plane normal   0.894 0.447 0.000
Symmetry Operation Matrix                            Shift 
  -1.000000000  -0.000000000   0.000000000           0.000000000
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000   1.000000000           0.000000000

19  120-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

20  240-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   1.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

21  60-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
  -1.000000000   1.000000000   0.000000000           0.000000000
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

22  300-degree Rotoinversion Operation about axis   0.000 0.000 1.000
Symmetry Operation Matrix                            Shift 
   0.000000000  -1.000000000   0.000000000           0.000000000
   1.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000

23  Inversion Operation
Symmetry Operation Matrix                            Shift 
  -1.000000000   0.000000000   0.000000000           0.000000000
   0.000000000  -1.000000000   0.000000000           0.000000000
   0.000000000   0.000000000  -1.000000000           0.000000000
```
</details>
<br>
