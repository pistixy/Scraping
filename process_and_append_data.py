import re

def process_and_append_data(input_filename, intermediate_filename, append_to_filename):
    # Open the input file and append its contents to the final output file
    with open(input_filename, "r", encoding="utf-8") as input_file, open(append_to_filename, "a", encoding="utf-8") as final_file:
        for line in input_file:
            final_file.write(line)

    # Process and format the data from the intermediate file
    processed_data = []
    with open(intermediate_filename, "r", encoding="utf-8") as intermediate_data:
        for line in intermediate_data:
            values = line.strip().split(',')

            # Extract the material and price
            material = values[0].strip()
            price = values[1].strip()

            # Remaining values and regex to find name, formula, purity, and dimensions
            remaining = ' '.join(values[2:])
            name_match = re.search(r"([\w\s]+)TARGET", remaining)
            formula_match = re.search(r", ([\w\s/%]+),", remaining)
            purity_match = re.search(r"([\d.]+% PURE)", remaining)
            dimensions_match = re.search(r"([\d.]+\"\s?DIAMETER\sX\s[\d.]+\"\s?THICK)", remaining)

            # Extracting the matched values
            name = name_match.group(1).strip() if name_match else "N/A"
            formula = formula_match.group(1).strip() if formula_match else "N/A"
            purity = purity_match.group(1).strip() if purity_match else "N/A"
            dimensions = dimensions_match.group(1).strip() if dimensions_match else "N/A"

            # Format the processed data
            processed_line = f"{material},{price},{name},{formula},{purity},{dimensions}\n"
            processed_data.append(processed_line)

    # Append the processed data from the intermediate file to the final output file
    with open(append_to_filename, "a", encoding="utf-8") as final_file:
        final_file.writelines(processed_data)

    print(f"Data from {input_filename} appended to {append_to_filename}, data from {intermediate_filename} processed and appended to {append_to_filename}")

