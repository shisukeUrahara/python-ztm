import sys
import os
from PIL import Image

# grab first and second argument
zero_argument= sys.argv[0]
image_folder= sys.argv[1]
output_folder= sys.argv[2]

print(image_folder)
print(output_folder)
print(zero_argument)
# check if new/ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created {output_folder} folder")
else:
    print(f"{output_folder} folder already exists")

# loop through Pokedex, convert images to png
for filename in os.listdir(image_folder):
    img= Image.open(f'{image_folder}/{filename}')
    clean_name= os.path.splitext(filename)[0]
    img.save(f'{output_folder}/{clean_name}.png', 'PNG')
    print(f"Converted {filename} to {clean_name}.png")

print("All images converted")