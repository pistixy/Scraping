def extract_description_data(description):
    # Initialize variables for name, purity, and rest of the description
    name = ""
    purity = ""
    rest = ""
    material_names=['Aluminum', 'Barium', 'Calcium', 'Cerium', 'Chromium', 'Copper', 'Hafnium', 'Indium', 'Iron', 'Magnesium', 'Molybdenum', 'Neodymium', 'Silicon', 'Strontium', 'Tantalum', 'Tin', 'Tungsten', 'Zinc', 'Zirconium']

    # Split the description into parts
    parts = description.split()
    
    if parts:
        # Extract the name (first part)
        name = parts[1]  # Assuming that the name is always the second part

        # Extract the purity enclosed in parentheses
        for part in parts:
            if "(" in part and ")" in part:
                purity = part.strip("()")
                break

        # Extract the rest of the description (excluding name and purity)
        rest = " ".join(parts[2:])  # Assuming that name and purity are always at the beginning

        for material in material_names:
            if material in description:
                name = material
                break
        
    return name, purity, rest


def clean_and_write_data(product_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        # Write the headers
        file.write("Material\tPurity\tPrice\tDescription\n")

        for product in product_data:
            # Initialize empty strings for each piece of information
            name, purity, price, rest = '', '', '', ''

            # Split the description into parts, assume they are separated by spaces
            name,purity,rest= extract_description_data(product['description'])
            

            # Write the extracted data to the file
            file.write(f"{name}\t{purity}\t{product['price']}\t{rest}\n")
