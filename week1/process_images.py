import os
import sys
import imghdr
from PIL import Image

# Set input and output directories
input_dir = 'images/'
output_dir = '/opt/icons/'

# Iterate over all files in the input directory
for filename in os.listdir(input_dir):
    # Check if file is an image file using imghdr
    image_type = imghdr.what(os.path.join(input_dir, filename))
    if image_type:
        # Open image using PIL
        with Image.open(os.path.join(input_dir, filename)) as im:
            # Rotate image 90 degrees clockwise
            im = im.rotate(-90, expand=True)
            # Resize image to 128x128
            im = im.resize((128, 128))
            # Split filename into base name and extension
            filename, ext = os.path.splitext(filename)
            # Save image to output directory with same name as input file, but without extension
            output_path = os.path.join(output_dir, filename)
            im = im.convert('RGB')
            im.save(output_path)
    else:
        print(f'Skipping file: {filename} as it is not an image file.')
