import re

def process_data(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            parts = line.split(',')

            # Initialize variables for each field and for the rest of the data
            name, material, formula, purity, diameter, thickness, price, rest = 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', []

            # Process each part to fill the variables
            for part in parts:
                part = part.strip()
                if 'TARGET' in part and material == 'N/A':
                    material = part
                elif '%' in part and purity == 'N/A':
                    purity = part
                elif 'DIAMETER' in part or 'x' in part or 'X' in part or '"' in part or 'dia' in part or 'MM' in part:
                    diameter_match = re.search(r'([\d.]+")', part)
                    if diameter_match:
                        diameter = diameter_match.group(1)
                    if 'x' in part or 'X' in part:
                        thickness_match = re.search(r'x\s*([\d.]+["MM]*)', part)
                        if thickness_match:
                            thickness = thickness_match.group(1)
                elif 'THICK' in part and thickness == 'N/A':
                    thickness = part
                elif ('€' in part or 'P.O.R.' in part) and price == 'N/A':
                    price = part
                elif formula == 'N/A':
                    formula = part
                else:
                    rest.append(part)

            # Join the rest of the data into a single string
            rest = ' '.join(rest)

            # If name is not determined from the parts, use the first part as the name
            if name == 'N/A' and len(parts) > 0:
                name = parts[0].strip()

            # Write the processed data to the output file in the specified order
            outfile.write(f"{name},{material},{formula},{purity},{diameter},{thickness},{price},{rest}\n")

    print(f"Data processing complete. Output saved to {output_filename}")

# File paths
input_filename = "D:/PhotonExport/Scraping/data/raw_data.txt"
output_filename = "D:/PhotonExport/Scraping/data/output.txt"

# Process the data
process_data(input_filename, output_filename)
def convert_to_mm(value):
    if '"' in value:  # Convert from inches to mm
        numeric_value = float(value.replace('"', ''))
        return numeric_value * 25.4
    elif 'MM' in value.upper():  # Already in mm, just extract the number
        return float(re.search(r'([\d.]+)', value).group(1))
    else:
        return 'N/A'  # In case the value is not in a recognized format

def add_mm_columns(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            parts = line.strip().split(',')

            if len(parts) >= 7:  # Ensure there are enough columns
                diameter, thickness = parts[4], parts[5]

                # Convert diameter and thickness to mm
                diameter_mm = convert_to_mm(diameter)
                thickness_mm = convert_to_mm(thickness)

                # Insert the converted values into the correct positions
                parts.insert(5, str(thickness_mm))
                parts.insert(4, str(diameter_mm))

            outfile.write(','.join(parts) + '\n')

    print(f"Data processing with added MM columns complete. Output saved to {output_filename}")

# File paths
input_filename = "D:/PhotonExport/Scraping/data/output.txt"
output_filename = "D:/PhotonExport/Scraping/data/output_with_mm.txt"

# Process the data
add_mm_columns(input_filename, output_filename)
