# Problem 1: Extract Image Information and Write to CSV<br />
Objective: Extract image name, size, and modification date for each image in a folder and write this data to a CSV file.<br />

Documentation:<br />

  1- Ensure you have Python installed on your system.<br />
  2- Place the images you want to process in the specified image folder (update the image_folder path in the code).<br />
  3- Run the provided Python script.<br />
  4- The script will iterate through the images in the folder and gather information about each image (name, size, and modification date).<br />
  5- The gathered data will be written to a CSV file named image_data.csv in the same directory as the script.<br />
Code Improvements:<br />

  --> Include necessary imports at the beginning of the code.<br />
  --> Use the os.path.splitext() function to extract file extensions.<br />
  --> Consider using a Path object from the pathlib module for better path manipulation.<br />
# Problem 2: Object Detection and JSON Output<br />
Objective: Detect objects in an image, extract object dimensions, and save the information in a JSON file.<br />

Documentation:<br />

  1- Install the required packages using pip install ultralytics.<br />
  2- Ensure you have an image named objects.png in the specified location (/content/objects.png in this case).<br />
  3- Run the provided code in a Jupyter Notebook or a compatible environment.<br />
  4- The code will perform object detection using YOLOv8 model and OpenCV's Haar Cascade Classifier.<br />
  5- Detected objects' dimensions (width and height) will be collected.<br />
  6- The results will be saved in results.txt in the same directory.<br />
  7- The script will then create a JSON file named object_dimensions.json containing the dimensions data.<br />
Code Improvements:<br />

  --> Include necessary imports at the beginning of the code.<br />
  --> Avoid unnecessary or repeated code blocks.<br />
  --> Make sure the paths for input and output files are correct and accessible.<br />
Remember to replace any specific paths, URLs, or filenames with the actual paths and names relevant to your environment. Also, make sure that you're using compatible versions of libraries and tools.

Finally, ensure that you've provided all necessary dependencies, such as YOLOv8 model files, Haar Cascade XML files, and other required resources, in the appropriate locations.
