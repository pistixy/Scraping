def process_data(input_filename, output_filename):
    material_list = ['Aluminum', 'Antimony', 'Barium', 'Bismuth', 'Boron', 'Calcium', 'Cerium', 'Chromium', 'Cobalt', 'Copper', 'Dysprosium', 'Erbium', 'Gadolinium', 'Germanium', 'Gold', 'Hafnium', 'Indium', 'Iridium', 'Iron', 'Lead', 'Lithium', 'Magnesium', 'Manganese', 'Molybdenum', 'Nickel', 'Niobium', 'Osmium', 'Palladium', 'Platinum', 'Potassium', 'Ruthenium', 'Silver', 'Sodium', 'Tantalum', 'Tin', 'Titanium', 'Tungsten', 'Uranium', 'Vanadium', 'Yttrium', 'Zirconium']

    with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        # Write the header to the output file
        outfile.write('Material,Name,Formula,Purity,Price,Quantity,Rest\n')

        for line in infile:
            parts = line.strip().split(',')
            name, material, purity, dimensions, quantity, price, rest = 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', []

            # Process to find the name
            for part in parts:
                part_cleaned = part.strip()
                if 'PELLETS' in part or 'WIRE' in part or 'CANES' in part or 'CRIMP' in part or 'SHOT' in part or 'ROD' in part or 'TABLETS' in part or 'PIECES' in part:
                    name = part_cleaned
                    parts.remove(part)
                    break

            # Process to find the material
            for part in parts:
                part_cleaned = part.strip()
                if any(mat in part_cleaned for mat in material_list):
                    material = part_cleaned
                    parts.remove(part)
                    break
            
            for part in parts:
                part_cleaned = part.strip()
                # Assuming you have a list of materials called 'material_list'
                if ('% PURE' in part or 'PURE'in part or '% pure' in part or '% Pure' in part):
                    purity = part_cleaned
                    parts.remove(part)  # Remove the material part from the list
                    break  # Break out of the loop once the material is found
            
            for part in parts:
                part_cleaned = part.strip()
                # Assuming you have a list of materials called 'material_list'
                if ('DIAMETER' in part or 'DIA'in part or 'dia' in part or 'LONG' in part or 'lenght' in part or 'long'in part or 'dia.' in part or 'LONG' in part):
                    dimensions = part_cleaned
                    parts.remove(part)  # Remove the material part from the list
                    break  # Break out of the loop once the material is found

            for part in parts:
                part_cleaned = part.strip()
                # Assuming you have a list of materials called 'material_list'
                if ('gram' in part or 'GRAM'in part or 'G' in part or 'pb' in part or 'lb' in part or 'lbs'in part or 'KILOGRAM.' in part or 'kg' in part or 'KG' in part):
                    quantity = part_cleaned
                    parts.remove(part)  # Remove the material part from the list
                    break  # Break out of the loop once the material is found

            for part in parts:
                part_cleaned = part.strip()
                # Assuming you have a list of materials called 'material_list'
                if ('P.O.R' in part or 'p.o.r'in part or '€' in part):
                    price = part_cleaned
                    parts.remove(part)  # Remove the material part from the list
                    break  # Break out of the loop once the material is found
            
            # Collecting the rest of the data
            rest = ' '.join(parts)  # Join the remaining parts with a comma

            # Write the processed data to the output file
            outfile.write(f"{material},{name},{purity},{dimensions},{quantity},{price},{rest}\n")

    print(f"Data processing complete. Output saved to {output_filename}")
    return True
