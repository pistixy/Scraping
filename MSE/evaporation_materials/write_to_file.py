def write_to_file(array, file_path):
    """
    Write the contents of an array to a text file, with each element on a new line.

    :param array: List of data to write to the file.
    :param file_path: The path to the text file to write to.
    """
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            for item in array:
                file.write(f"{item}\n")
        print(f"Data has been written to {file_path}")
    except IOError as e:
        print(f"An error occurred: {e}")
