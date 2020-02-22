import sys
import os
from PIL import Image


# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# print(image_folder, output_folder)
# os module to grab the path
# check if new folder exists, if not create it. Since we want to do something
# like python3 JPGtoPNGconverter.py Pokedex/  new/
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through Pokedex
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print("all done!")


# convert images to PNG


# save to the new folder
