import numpy as np
from genVESTAfromPOSCAR.tools.color import numbers_to_red_blue_colors, number_to_red_blue_color
from genVESTAfromPOSCAR.tools.convertor import genVESTAfromPOSCAR
from genVESTAfromPOSCAR.tools.config import config_is_exist

def main():
    options = config_is_exist()
    
    # Set color ratio
    x = np.random.randint(100,size=97)-50
    #x = 8 * [-0.5]  + 40 * [0] + 24 * [1] + 16 * [0] + 8 * [-1] + [0.5]
    
    # Preparing color values
    R, G, B = numbers_to_red_blue_colors(x)
    C = np.array([R, G, B])
    C = C.swapaxes(0,1)

    
    genVESTAfromPOSCAR(filename=options["target file"],savename=options["result name"],color_data=C)
    print(f"{options["target file"]} is converted to {options["result name"]}")