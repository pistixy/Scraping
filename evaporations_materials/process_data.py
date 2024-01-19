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
    return True