# You need to read "replacement_needed.txt" file. This file has one mistake. One letter needs
# to be replaced with other letter then this sentence might have some meaning. Replace this
# letter with the desired one making logic yourself without using any library. Write your code
# in function and call that function. Handle all possible exceptions as well.

# Name: Rija Ali
# ID:23k-0057

def replacement(filename,replacement_word,old_word):
    try:
         with open (filename , 'r') as file:
              content = file.read()
              replacement_text = content.replace( old_word , replacement_word)
         with open(filename , 'w') as file:
              file.write(replacement_text)
         print(f" '{old_word}' has been replaced with: '{replacement_word}'")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filename}'.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

replacement_word = 'h'
old_word = 'f'
filename = 'replacement_needed.txt'

replacement(filename,replacement_word , old_word)

            
