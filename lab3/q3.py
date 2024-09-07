# Write a python program that takes any two lists from user having same number of
# elements. Make a dictionary from these two lists in such a way that first element of first list
# will be key and first element of second list will be its associated value and so on. Store the
# dictionary in a text file. Handle all possible exceptions as well.

# Name: Rija Ali
# ID: 23k-0057

def list_to_dict(filename ):

    list1 = input("Enter the first lsit (space-separated): ").split() #.split() to conver a string into sub strings
    list2 = input("Enter the first lsit (space-separated): ").split()

    try:
        if len(list1) != len(list2):
            print("Error! both lists must be of the same size")
            return
    
        dictionary = dict(zip(list1,list2)) #creating dictionary from user-input of lists

    except Exception as e:
        print(f"Unexpected error occured: {e}")

    
    else:
        try:
            with open(filename , 'w') as file:
                 for key, value in dictionary.items(): #.itmes() to view the key and value as a pair and for loop to iterate till the list items finish
                    file.write(f"{key}: {value}\n") 
                 print(f"Dictionary has been written to '{filename}'.")
        except PermissionError:
            print(f"Error: Permission denied to write to the file '{filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred while writing to the file: {e}")

        # except Exception as e:
        #     print(f"Unexpected error occurred: {e}")

filename = 'q3.txt'

list_to_dict(filename)

