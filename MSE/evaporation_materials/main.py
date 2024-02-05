from write_to_file import write_to_file
from extract_product_data import extract_product_data
from get_links import get_links
from copy_all_files import copy_all_files, get_latest_timestamp_folder, get_timestamp
from is_folder_empty import is_folder_empty, create_folder
from clean_and_write_data import clean_and_write_data
from copy_output_to_data import copy_output_to_data

# Define the base folder path relative to the current script location
base_folder_path = "MSE/evaporation_materials/data"
base_url = 'https://www.msesupplies.com/collections/evaporation-materials?page='
output_filename = "output.txt"

# Get the current timestamped folder name
current_folder = get_timestamp()

# Check if the base folder is empty, if so, create a new timestamped folder
if is_folder_empty(base_folder_path):
    create_folder(f"{base_folder_path}/{current_folder}")
else:
    # If it's not empty, copy all files from the latest timestamped folder to the new one
    copy_all_files(f"{base_folder_path}/{get_latest_timestamp_folder(base_folder_path)}",
                   f"{base_folder_path}/{current_folder}")

# Define the full path to the current folder
folder_path = f"{base_folder_path}/{current_folder}"

# Get the URLs for pages 1 through 6
links = get_links(base_url, 1, 6)

# Initialize an empty list to hold all product data
all_product_data = []

# Iterate through the links and extract product data
for link in links:
    product_data = extract_product_data(link)

    all_product_data.extend(product_data)  # Combine data from all pages
clean_and_write_data(all_product_data,f"{folder_path}/{output_filename}")
copy_output_to_data(f"{folder_path}",base_folder_path,"output.txt")
    
# Write the product data to a file within the current timestamped folder
#write_to_file(all_product_data, f"{folder_path}/{output_filename}")


