def employee_biodata():
    try:
        name = input("Enter employee name: ")
        cnic = input("Enter CNIC number: ")
        age = int(input("Enter age: "))
        salary = float(input("Enter salary: "))
        return name, cnic, age, salary
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter the correct data type.")
        return None


def biodata_to_file_save(filename, biodata):
    try:
        with open(filename, 'w') as file:
            name, cnic, age, salary = biodata
            file.write(f"Name: {name}\n")
            file.write(f"CNIC Number: {cnic}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Salary: {salary}\n")
        print(f"Biodata has been saved to '{filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while saving biodata: {e}")


def contact_number(filename):

    try:
        contact_number = input("Enter contact number: ")
        with open(filename, 'a') as file:
            file.write(f"Contact Number: {contact_number}\n")
        print(f"Contact number has been appended to '{filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while appending contact number: {e}")


def read_file(filename):

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")


def main():
    filename = 'biodata.txt'

    # Collect biodata from the user
    biodata = employee_biodata()
    if biodata:
        # Save biodata to file
        biodata_to_file_save(filename, biodata)

        # Append contact number to file
        contact_number(filename)

        # Read and display the file contents
        read_file(filename)


if __name__ == "__main__":
    main()
