import os
import shutil

# Set the source directory (where the folders are located)
source_directory = "C:/Users/ttian/Downloads/2024 ICLEF Materials"  # Change this to your actual source folder
# Set the destination directory (where all PDFs will be copied)
destination_directory = "C:/Users/ttian/Downloads/ICLEF to be uploaded"  # Change this to your actual destination folder

# Ensure the destination folder exists
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

for root, _, files in os.walk(source_directory):
    for file in files:
        if file.endswith(".pdf"):
            source_path = os.path.join(root, file)
            
            # Extract the folder name
            folder_name = os.path.basename(root)
            
            # Create new file name with folder name as prefix
            new_filename = f"{folder_name}_{file}"
            destination_path = os.path.join(destination_directory, new_filename)
            
            # Handle duplicate filenames
            counter = 1
            while os.path.exists(destination_path):
                name, ext = os.path.splitext(new_filename)
                destination_path = os.path.join(destination_directory, f"{name}_{counter}{ext}")
                counter += 1
            
            # Copy the file with the new name
            shutil.copy2(source_path, destination_path)

print("All PDFs have been copied successfully with folder names prefixed!")

