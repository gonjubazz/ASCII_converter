import math
from PIL import Image

image = input()

image = Image.open(image)
size = image.size

width, height = size
ratio = width / height
new_height = 330

new_width = int(ratio * new_height)
            
image = image.resize((new_width, new_height))
size = image.size

gray_scale = list(" .:-=+*#%@")

for y in range(size[1]):
    for x in range(size[0]):
    
        color = image.getpixel((x, y))
        r = color[0]
        g = color[1]
        b = color[2]
        
        Y=0.3*r+0.59*g+0.11*b+0.01
        
        print(gray_scale[math.ceil(Y/25.6)-1], end="  ")
    print("")