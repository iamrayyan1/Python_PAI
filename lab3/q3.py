def list(prompt):
    while True:
        try:
            user_input = input(prompt)
            list_from_user = user_input.split()
            return list_from_user
        except Exception as e:
            print(f"Error: {e}. Please enter the list again.")


def dict_lists(keys_list, values_list):
    return dict(zip(keys_list, values_list))


def dict_file(filename, dictionary):
    try:
        with open(filename, 'w') as file:
            for key, value in dictionary.items():
                file.write(f"{key}: {value}\n")
        print(f"Dictionary has been written to '{filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while writing to the file: {e}")


def main():
    try:
        # Get two lists from the user
        list1 = list("Enter the first list of keys (space-separated): ")
        list2 = list("Enter the second list of values (space-separated): ")

        # Check if both lists have the same number of elements
        if len(list1) != len(list2):
            print("Error: Both lists must have the same number of elements.")
            return

        # Create dictionary from the two lists
        dictionary = dict_lists(list1, list2)

        # Write the dictionary to a text file
        filename = 'q3.txt'  # You can choose a different filename
        dict_file(filename, dictionary)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the main function
if __name__ == "__main__":
    main()
