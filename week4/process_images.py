# path to .tiff images => /supplier-data/images


#!/usr/bin/env python3
from PIL import Image
import os

input_path = 'supplier-data/images/'
output_path = 'supplier-data/images/'


# Iterate over all files in the input path
for filename in os.listdir(input_path):
    # Check if the file is a TIFF image
    if filename.endswith('.tiff'):
        # Open the image
        with Image.open(os.path.join(input_path, filename)) as img:
            # Resize the image
            img = img.resize((600, 400))

            # Convert the image to RGB format
            img = img.convert('RGB')

            # Save the image as JPEG
            output_filename = os.path.splitext(filename)[0] + '.jpeg'
            output_file_path = os.path.join(output_path, output_filename)
            img.save(output_file_path, format='JPEG')

            print(f'Processed {filename} -> {output_filename}')
