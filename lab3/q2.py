def replace(filename, search, new):
    try:
        # Read the content of the file
        with open(filename, 'r') as file:
            file_content = file.read()

        modified_content = file_content.replace(search, new)

        with open(filename, 'w') as file:
            file.write(modified_content)

        print(f"All occurrences of '{search}' have been replaced with '{new}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filename}'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
filename = 'q2.txt'  # Replace with your file path
search = 'rija'  # Replace with the phrase you want to search for
new = 'world'  # Replace with the phrase you want to use as replacement

replace(filename, search, new)
