import re
import shutil

import re


def process_data2(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            values = line.strip().split(',')

            # Initialize variables for each field
            material, price, target, formula, purity, dimensions, rest = '', '', '', '', '', '', ''

            # Extract material and price
            if len(values) > 1:
                material, price = values[0].strip(), values[1].strip()

            # Find and extract the remaining values
            for value in values[2:]:
                if 'TARGET' in value:
                    target = value.strip()
                elif '% PURE' in value:
                    purity = value.strip()
                elif '%' in value or len(value.strip()) <= 5:
                    formula = value.strip()
                elif any(x in value for x in ['THICK', 'DIAMETER', '"', 'MM']):
                    dimensions = value.strip()
                else:
                    rest += value.strip() + ' '

            # Write the formatted line to the output file
            outfile.write(f"{material},{price},{target},{formula},{purity},{dimensions},{rest.strip()}\n")

    print(f"Data processing complete. Output saved to {output_filename}")




def append_data(source_filename, destination_filename):
    # Append the contents of the source file to the destination file
    with open(source_filename, "r", encoding="utf-8") as source_file, \
         open(destination_filename, "a", encoding="utf-8") as dest_file:
        shutil.copyfileobj(source_file, dest_file)
    print(f"Data from {source_filename} appended to {destination_filename}")

