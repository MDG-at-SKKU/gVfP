# genVESTAfromPOSCAR

This program is written to represent the properties of atoms (e.g. magnetic moment) by the color of each atom.
* It takes the atomic structure as input (POSCAR, CIF, etc).
* Outputs a VESTA format file. (You can open the file using the VESTA program and make adjustments.)
* Requires data to specify the color. (Red for positives, blue for negatives, white for 0.)

## Installation

* Requires `python  >= 3.13`
```
git clone https://github.com/MDG-at-SKKU/gVfP.git
cd gVfP
pip install -e .
gvfp
```

* For the first time, `gVfP_config.ini` will be generated automatically.
  
## How to use

* Set `gVfP_config.ini`

```
[Data Info]
# target file : path of target file.  ex) POSCAR or Dataset/POSCAR # Default(blank) is POSCAR
target file =

[Color Setting]
# color list file : path of color list file. Default(blank) is blank. It will set color randomly
# IMPORTANT : Number of colors and number of atoms should be a same number
color list file = color.txt

[Result File Option]
# result name : setting name of output file. # Default(blank) is POSCAR.vesta
result name =

[Version]
version = 0.0.2
```

* Set `input file`. If the name of your input structure file is `POSCAR`, you don't have to specify. Indeed, you can open any structure file that the Atomic Simulation Environment (ASE) can open, other than `POSCAR` files (e.g. CIF). 

* Prepare a file containing real numbers for every atom (e.g. `color.txt`), and set the name of the data file (for specifying color) in the `gVfP_config.ini` file. If not set, a random color is assigned.  

File format examples:
```
-9
26.0
-31.2
-8
-22
-12
0
4
-20
-40
-7
...
```

* Set `result name`. If not, a `POSCAR.vesta` file will be created.

* Run `gvfp` again, and draw the generated vesta file using the VESTA program.

## Link
[Materials Design Group @ SKKU](https://sites.google.com/site/jsparkphys/home)
