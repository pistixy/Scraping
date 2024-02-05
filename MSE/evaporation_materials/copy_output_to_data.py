import os
import shutil

def copy_output_to_data(src_directory, dest_directory, file_name="output.txt"):
    # Assuming src_directory is the full path to the latest folder
    if src_directory:
        source_file = os.path.join(src_directory, file_name)
        destination_file = os.path.join(dest_directory, file_name)

        # Check if the source file exists
        if os.path.exists(source_file):
            # Ensure the source and destination are not the same
            if os.path.abspath(source_file) != os.path.abspath(destination_file):
                shutil.copy(source_file, destination_file)
                print(f"Copied '{file_name}' from {src_directory} to {dest_directory}")
            else:
                print("Source and destination are the same. No action taken.")
        else:
            print(f"'{file_name}' not found in {src_directory}")
    else:
        print("Source directory is not specified.")

