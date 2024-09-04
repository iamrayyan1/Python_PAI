def char_word_count(filename):
    try:
        with open(filename) as file:
            file_content = file.read()
            file_content = file_content.replace(' ' , '')
            char_count = len(file_content)
            word_count = len(file_content.split())
            print(f"Total number of characters: {char_count}")
            print(f"Total number of words: {word_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
filename = 'q1.txt'
char_word_count(filename)
