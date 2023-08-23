import os
import csv
from datetime import datetime
# Path to the folder containing the images
image_folder = 'C:/Users/E CORP/Downloads/problem1/images'

# List to store image data
image_data = []

# Iterate through the files in the folder
for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):  # Add more extensions if needed
        filepath = os.path.join(image_folder, filename)
        image_size = os.path.getsize(filepath)  # Get image size in bytes
        modification_date_timestamp  = os.path.getmtime(filepath)  # Get modification date as a timestamp
        modification_date = datetime.fromtimestamp(modification_date_timestamp).strftime('%a %b %d %H:%M:%S %Y')
        image_data.append([filename, image_size, modification_date])

# Path to the CSV file
csv_file_path = 'image_data.csv'

# Write data to the CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['image_name', 'image_size', 'modification_date'])  # Write header row
    csv_writer.writerows(image_data)  # Write image data

print(f"CSV file '{csv_file_path}' has been created.")
