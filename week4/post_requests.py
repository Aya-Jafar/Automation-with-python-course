#!/usr/bin/env python3

import os
import requests

# Specify the directories where the text files and images are located
description_directory = 'supplier-data/descriptions/'
image_directory = 'supplier-data/images/'

# Iterate over all text files in the directory
for filename in os.listdir(description_directory):
    if filename.endswith('.txt'):
        # Open the file for reading
        with open(os.path.join(description_directory, filename), 'r') as f:
            # Read the file contents and extract the relevant data
            lines = [line.rstrip() for line in f]
            content = {
                'name': lines[0],
                'weight': int(lines[1].split()[0]),
                'description': lines[2],
                'image_name': os.path.splitext(filename)[0] + '.jpeg'
            }

        # Send the POST request with the data and the image file
        with open(os.path.join(image_directory, content['image_name']), 'rb') as image_file:
            response = requests.post(
                'http://34.133.124.157/fruits/',
                data=content,
                files={'image': image_file}
            )
            print(response.status_code)
