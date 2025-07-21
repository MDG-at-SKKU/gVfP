import numpy as np

def number_to_red_blue_color(ratio):
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
        r, g, b = number_to_red_blue_color(numbers[i])
        R.append(r)
        G.append(g)
        B.append(b)
    return(R, G, B)  
