# genVESTAfromPOSCAR

This program is written to represent the properties of each atom (e.g. magnetic moment) by the color of each atom.
* It takes the atomic structure as input (POSCAR, CIF, etc).
* Outputs a VESTA format file.
* Requires data sorted by atomic number to specify the color. (Red for positives, blue for negatives, white for 0.)

## How to use

```
git clone https://github.com/MDG-at-SKKU/gVfP.git
cd gVfP
pip install -e .
gvfp
```

First time, `gVfP_config.ini` will be generated automatically.

If the name of your input structure file is `POSCAR`, run gVfp again. A `POSCAR.vesta` file will be created. 

Indeed, you can open any structure file that the Atomic Simulation Environment (ASE) can open, other than `POSCAR` files (e.g. CIF). In this case, open `gVfP_config.ini` and modify the target file and result name.


## Optional
### Setting a color list file
Example of color list file
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

## Link
[Materials Design Group @ SKKU](https://sites.google.com/site/jsparkphys/home)
