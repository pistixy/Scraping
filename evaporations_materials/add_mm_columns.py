import re

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
    return True

