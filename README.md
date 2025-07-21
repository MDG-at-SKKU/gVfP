# genVESTAfromPOSCAR

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

## Link
[Materials Design Group @ SKKU](https://sites.google.com/site/jsparkphys/home)
