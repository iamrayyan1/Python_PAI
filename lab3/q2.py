# Create a program that reads a text file, searches for a specified word or phrase, and replaces
# all occurrences with another word or phrase. Write the modified content back to the file.
# Handle all possible exceptions as well.

# Name: Rija Ali
# ID: 23k-0057

def replace(filename, search, new):
    try:
        # Read the content of the file
        with open(filename, 'r') as file:
            file_content = file.read()

        modified_content = file_content.replace(search, new) #.replace() to replace old word with new word

        with open(filename, 'w') as file: #opening file as w to write in a file
            file.write(modified_content) 

        print(f"All words containing '{search}' have been replaced with '{new}'.")
    
    #exception handling
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filename}'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


filename = 'q2.txt' 
search = 'rija'  
new = 'world'  

replace(filename, search, new)
