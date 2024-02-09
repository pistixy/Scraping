def process_dimensions(input_file, output_file):
    quantities = [
    "50 g", "100 g", "250 g", "1 kg",
    "25 g", "50 g", "100 g", "250 g", "79mg", "300 GRAMS",
    "500 g", "1 POUND", "25 g", "50 g", "25 GRAMS", "50 GRAMS", "1 kilogram",
    "100 g", "250 g", "2 lbs", "75 g",  "200g", "500g", "PER FOOT", "per foot", "100g"
    "300 g", "0.5 kg", "10 g", "20 lb","139 mg","40 mg","25 mg","35 mg","406 mg","PER GRAM", "per gram", "per g", "SOLD BY THE FOOT",
    "30 g", "40 g", "1.5 kg", "200 g", "ONE POUND", "2 pounds","24-lb", "24 POUNDS", "1 lb.", "400 mg", "406 mg", "400mg", "406mg"
]
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
                
            quantity=""    
            for i in quantities:
                if i.lower() in parts[6].lower():
                    quantity=i
                    parts.insert(8, quantity)
                    break

            # Write the new line to the output file
            outfile.write(','.join(parts) + '\n')

    print(f"Processing complete. Output saved to {output_file}")

