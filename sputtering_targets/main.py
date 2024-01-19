from is_folder_empty import is_folder_empty, create_folder
from copy_all_files import get_timestamp, copy_all_files, get_latest_timestamp_folder
from get_links import get_links
from scrape_and_save_data import scrape_and_save_data
from process_data import process_data
from add_mm_columns import add_mm_columns
from add_column_names_to_file import add_column_names_to_file
from copy_output_to_data import copy_output_to_data
import os

base_folder_path="sputtering_targets/data"
url='https://www.lesker.com/materials-division.cfm?section=sputtering-targets'
extracted_links="extracted_links.txt"
raw_data="raw_data.txt"
processed_data="processed_data.txt"
output="sputtering_targets.txt"
final_output="final_output.txt"
column_names = ['Name', 'Material', 'Formula', 'Purity', 'Diameter mm', 'Diameter "', 'Thickness mm', 'Thickness "', 'Price', 'Rest']

current_folder=get_timestamp()
if (is_folder_empty(base_folder_path)):
    create_folder(base_folder_path +"/"+current_folder)
else:
    copy_all_files(base_folder_path +"/"+get_latest_timestamp_folder(base_folder_path),base_folder_path +"/"+current_folder)

folder_path=base_folder_path +"/"+current_folder

if (get_links(url,folder_path + "/" + extracted_links)):
    if (scrape_and_save_data(folder_path + "/" + extracted_links, folder_path + "/" + raw_data)):
        process_data(folder_path + "/" + raw_data, folder_path + "/" + processed_data)
        add_mm_columns(folder_path + "/" + processed_data,  folder_path + "/" + output)
        add_column_names_to_file(folder_path + "/" + output, column_names)
        print("Successful scraping!")
        copy_output_to_data(base_folder_path +"/" + current_folder, base_folder_path, file_name=output)

