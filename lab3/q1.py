# Write a Python program that reads a text file, counts the number of characters in it, and
# prints the total word count. Handle all possible exceptions as well.

# Name: Rija Ali
# ID: 23k-0057

def char_word_count(filename):
    try:
        with open(filename) as file:
            file_content = file.read()
            word_count = len(file_content.split()) #.split() method in Python is used to split a string into a list of substrings 
            char_count = len(file_content.replace(' ' , '')) #.replace(' ' , '') to replace white-space with no space to count characters
            
            print(f"Total number of words: {word_count}")
            print(f"Total number of characters: {char_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

filename = 'q1.txt'
char_word_count(filename)
