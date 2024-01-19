def add_column_names_to_file(filename, column_names):
    # Read the existing content of the file
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Column names as a string, comma-separated
    column_names_str = ','.join(column_names)

    # Open the file in write mode and prepend the column names
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(column_names_str + '\n' + content)
    
    print("Couloumn names added to: ", filename)
    return True


