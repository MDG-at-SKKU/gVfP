import numpy as np
from genVESTAfromPOSCAR.tools.convertor import genVESTAfromPOSCAR
from genVESTAfromPOSCAR.tools.config import config_is_exist

def main():
    config = config_is_exist()

    genVESTAfromPOSCAR(options=config)
    print(f"{config["target file"]} is converted to {config["result name"]}")