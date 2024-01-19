import os
import shutil
from datetime import datetime

def get_timestamp():
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time as a string in the desired format
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    
    return timestamp

def copy_all_files(source_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Copy each file from the source folder to the destination folder
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)

        # Check if it's a file and not a directory
        if os.path.isfile(source_file):
            shutil.copy(source_file, destination_file)

    print(f"All files from {source_folder} have been copied to {destination_folder}")


def get_latest_timestamp_folder(directory):
    # List all subdirectories in the specified directory
    subdirs = [os.path.join(directory, d) for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

    # Parse the folder names as datetime objects and sort them
    sorted_folders = sorted(subdirs, key=lambda x: datetime.strptime(os.path.basename(x), "%Y-%m-%d_%H-%M-%S"), reverse=True)

    # Return the latest folder (first in the sorted list)
    if sorted_folders:
        return os.path.basename(sorted_folders[0])
    else:
        return None