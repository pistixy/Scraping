def process_dimensions(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        # Read the header and write it back into the output file
        # Assuming the first line is the header
        header = infile.readline().strip()
        outfile.write(header + ",Diameter,Length\n")

        for line in infile:
            parts = line.strip().split(',')
            dimensions_data = parts[3].lower()  # Lowercase to handle different cases

            # Possible separators for dimensions
            separators = [' x ', 'x', '*', ' by ', '×']

            # Initialize diameter and length as 'N/A'
            diameter = 'N/A'
            length = 'N/A'

            # Iterate through possible separators to find a match
            for sep in separators:
                if sep in dimensions_data:
                    dimensions_parts = dimensions_data.split(sep)
                    if len(dimensions_parts) == 2:
                        # Attempt to extract diameter and length if two parts are found
                        diameter_part = dimensions_parts[0]
                        length_part = dimensions_parts[1]
                        # Here, you might need additional logic to extract the numeric values
                        # For simplicity, let's assume the diameter/length are always before the unit
                        diameter = ''.join(filter( None ,diameter_part))
                        length = ''.join(filter(None, length_part))
                        break

            # Replace or insert the diameter and length into the parts list
            parts[3] = diameter
            if len(parts) > 4:  # Check if there is a placeholder for length already
                parts[4] = length
            else:
                parts.insert(4, length)  # Insert length after diameter if not

            # Write the new line to the output file
            outfile.write(','.join(parts) + '\n')

    print(f"Processing complete. Output saved to {output_file}")

