# genVESTAfromPOSCAR

This program is written to represent the properties of atoms (e.g. magnetic moment) by the color of each atom.
* It takes the atomic structure as input (POSCAR, CIF, etc).
* Outputs a VESTA format file. (You can open the file using the VESTA program and make adjustments.)
* Requires data to specify the color. (Red for positives, blue for negatives, white for 0.)

## Installation

```
git clone https://github.com/MDG-at-SKKU/gVfP.git
cd gVfP
pip install -e .
gvfp
```
* `Python requires >= 3.13`
* For the first time, `gVfP_config.ini` will be generated automatically.
  
## How to use

### gVfP_config.ini

```
[Data Info]
# target file : path of target file.  ex) POSCAR or Dataset/POSCAR # Default(blank) is POSCAR
target file =

[Color Setting]
# color list file : path of color list file. Default(blank) is blank. It will set color randomly
# IMPORTANT : Number of colors and number of atoms should be a same number
color list file = 

[Result File Option]
# result name : setting name of output file. # Default(blank) is POSCAR.vesta
result name =

[Version]
version = 0.0.2
```

* If the name of your input structure file is `POSCAR`, you don't have to specify. Indeed, you can open any structure file that the Atomic Simulation Environment (ASE) can open, other than `POSCAR` files (e.g. CIF). In this case, open `gVfP_config.ini` and modify the target file and result name.

* Prepare a file containing real numbers (float) for every atom (e.g. `color.txt`). The name of the data file (for specifying color) must also be set in the same configuration file (`color list file`). If not set, a random color is assigned.  

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

* Run `gvfp` again.


## Link
[Materials Design Group @ SKKU](https://sites.google.com/site/jsparkphys/home)
