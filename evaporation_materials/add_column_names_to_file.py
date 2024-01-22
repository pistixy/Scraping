def add_column_names_to_file(file_path, column_names):
    # Check if the file is empty or if the first line is not the column names
    try:
        with open(file_path, 'r+', encoding='utf-8') as file:
            first_line = file.readline().strip()
            if not first_line or first_line.split(',') != column_names:
                # Go back to the start of the file after reading the first line
                file.seek(0, 0)
                # Read the rest of the file content after the first line
                content = file.read()
                # Go back to the start of the file to write column names and original content
                file.seek(0, 0)
                file.write(','.join(column_names) + '\n' + first_line + '\n' + content)
    except FileNotFoundError:
        # If the file does not exist, create it and write the column names
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(','.join(column_names) + '\n')
