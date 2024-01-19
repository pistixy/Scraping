import re

def extract_and_format_links(input_file_path, output_file_path):
    try:
        # Read lines from the input file
        with open(input_file_path, 'r') as file:
            lines = file.readlines()

        # Initialize an empty list to store the formatted links
        formatted_links = []

        # Loop over every line to extract URLs
        for line in lines:
            line = line.strip()
            # Check if the line contains the specific HTML tag
            if '<h2 class="h3 mb-4"><a href=' in line:
                # Extract the URL using regular expression
                match = re.search(r'href="([^"]+)"', line)
                if match:
                    # Prepend "https://www.lesker.com" to the extracted URL
                    formatted_link = "https://www.lesker.com" + match.group(1)
                    formatted_links.append(formatted_link)

        # Write the formatted links to the output file
        with open(output_file_path, 'w') as file:
            for link in formatted_links:
                file.write(link + '\n')
        print(f"Formatted links successfully extracted and saved to {output_file_path}")

    except IOError as e:
        print(f"An I/O error occurred: {e}")

    except re.error as e:
        print(f"A regular expression error occurred: {e}")


