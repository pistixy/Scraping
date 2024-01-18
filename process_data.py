import re

# Function to check if a string contains a number
def contains_number(s):
    return any(char.isdigit() for char in s)

def process_data(input_filename, output_correct, output_incorrect):
    # Open the input and output files with UTF-8 encoding
    with open(input_filename, "r", encoding="utf-8") as input_file, \
         open(output_correct, "w", encoding="utf-8") as correct_file, \
         open(output_incorrect, "w", encoding="utf-8") as incorrect_file:

        for line in input_file:
            values = line.strip().split(',')

            # Check the criteria for each record
            if (len(values) > 6 and
                values[0].strip() != "" and  # First column is not empty
                (values[1].strip() == "P.O.R." or re.match(r'\d+(\.\d+)?', values[1].strip())) and  # Second column is a price or 'P.O.R.'
                "TARGET" in values[2].upper().strip() and  # Third column contains 'TARGET' or 'target'
                values[3] == ' ' and values[5] == ' ' and
                values[4].strip() != "" and  # Fifth column is not empty
                (contains_number(values[6].strip()) and " PURE" in values[6].strip())):  # Sixth column contains a number followed by 'PURE'

                # Remove the fourth element (index 3)
                values.pop(3)
                values.pop(6)

                # Additional removals based on length
                if (len(values)==12):
                    values.pop(-1)
                if (len(values)==12):
                    values.pop(-1)
                if (len(values)==12):
                    values.pop(-1)
                if (len(values)==11):
                    values.pop(-1)
                
                if values[4]==' ':
                    values.pop(4)
                if len(values)>=7:
                    values.pop(6)

                # Truncate to the first 7 values
                values = values[:7]

                # Join the list back into a string
                line_to_write = ','.join(values)

                # Write the modified line to the correct file
                correct_file.write(line_to_write + '\n')
            else:
                incorrect_file.write(line)

    print("Formatting completed. Correct data saved to formatted_correct_data.txt and the rest to formatted_incorrect_data.txt")

