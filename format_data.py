import re

def format_data(input_filename, output_filename):
    # Open the input and output files with UTF-8 encoding
    with open(input_filename, "r", encoding="utf-8") as input_file, open(output_filename, "w", encoding="utf-8") as output_file:
        # Iterate through each line in the input file
        for line in input_file:
            # Remove Euro symbols (€) from the line
            line_without_euro = re.sub(r'€', '', line)

            # Split the line into individual values using commas as the separator
            values = line_without_euro.strip().split(',')
            
            # Extract specific fields
            material = values[0].strip()
            dimensions = values[-7].strip()
            purity = values[-6].strip()
            notes = values[-4].strip()
            price = values[-1].strip()
            
            # Combine the remaining data into the "rest" field
            rest = ", ".join(values[1:-7])
            separator=','
            
            # Create the formatted output line
            formatted_line = f"{material}{separator}{price}{separator}{rest}\n"
            
            # Write the formatted line to the output file
            output_file.write(formatted_line)

    # Print a message indicating the task is complete
    print(f"Formatting completed. Data saved to {output_filename}")


