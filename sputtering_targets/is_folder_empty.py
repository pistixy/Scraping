import os

def is_folder_empty(folder_path):
    # Returns True if the folder is empty, False otherwise
    return len(os.listdir(folder_path)) == 0

def create_folder(folder_path):
    # Check if the folder already exists
    if not os.path.exists(folder_path):
        # Create the folder
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")


