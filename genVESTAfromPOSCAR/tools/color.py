import numpy as np

def color_init(color_setting, length_n):
    if color_setting == "":
        # Set random color number
        arbitrary_int = np.random.randint(100,size=length_n)-50
        return arbitrary_int
    else:
        with open(f"{color_setting}", 'r') as color_file:
            color_num_li = color_file.readlines()
            color_num_li = [float(color_n_str) for color_n_str in color_num_li]
        if len(color_num_li) != length_n:
            raise Exception(f"Required length of color list is {length_n} but input has {len(color_num_li)}")
        else:
            return color_num_li


def number_to_red_blue_color_part(ratio):
    if ratio > 0:        
        red = 255
        green = 255 - int(np.round(255 * ratio))
        blue = 255 - int(np.round(255 * ratio))
    else:
        blue = 255
        red = 255 - int(np.round(-255 * ratio))
        green = 255 - int(np.round(-255 * ratio))
    return(red, green, blue)

def numbers_to_red_blue_colors(numbers):
    numbers = np.array(numbers)
    maxVal = np.abs(numbers).max()
    numbers = numbers / maxVal
    R, G, B = [], [], []
    for i in range(len(numbers)):
        r, g, b = number_to_red_blue_color_part(numbers[i])
        R.append(r)
        G.append(g)
        B.append(b)
    return(R, G, B)  

def color_rgb_list_generator(color_setting, length_n):
    color_num_list = color_init(color_setting, length_n)
    # Preparing color values
    R, G, B = numbers_to_red_blue_colors(color_num_list)
    color_final = np.array([R, G, B])
    color_final = color_final.swapaxes(0,1)
    
    return color_final