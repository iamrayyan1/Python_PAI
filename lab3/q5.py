
# Take input from user below dictionary having name and age pair. Save this dictionary in
# json file. Now load this json file and Print name of person having maximum age and also
# print if anyone has the same age by making logic yourself without using any library:
# dictionary = {'Ali': 23,'Saad':24,'Salman':15,'Shams':25,'Sadiq':46,'Hammad':23'}
# Handle all possible exceptions as well. 

# Name: Rija Ali
# ID: 23k-0057

import json

# Function to save dictionary to a JSON file
def saving_json(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Dictionary successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the dictionary: {e}")

def _json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except json.JSONDecodeError:
        print("Error: The file content is not a valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def max_age(data):
    try:
        if not data:
            print("The dictionary is empty, no person to find.")
            return

        max_age = max(data.values())
        people_max_age = [name for name, age in data.items() if age == max_age]

        if len(people_max_age) == 1:
            print(f"The person with the maximum age is: {people_max_age[0]}, Age: {max_age}")
        else:
            print(f"People with the maximum age ({max_age}) are: {', '.join(people_max_age)}")
    except Exception as e:
        print(f"An error occurred while finding the maximum age: {e}")


def main():
    dictionary = {'Ali': 23, 'Saad': 24, 'Salman': 15, 'Shams': 25, 'Sadiq': 46, 'Hammad': 23}
    filename = "q5.txt"

    saving_json(filename, dictionary)
    loaded_data = _json(filename)

    if loaded_data:
        max_age(loaded_data)


if __name__ == "__main__":
    main()
