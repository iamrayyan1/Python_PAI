# Create a function that asks the user to enter a sentence then writes the sentence to a text file
# named "questions.txt" if it's a question. Handle all possible exceptions as well.

# Name: Rija Ali
# ID: 23k-0057

def question_to_file(filename):

    try:

        sen = input("Enter a sentence: ").strip()

        # Checking if the sentence is a question
        if sen.endswith('?'):
            with open(filename, 'w') as file:
                file.write(sen + '\n')
            print(f"The sentence has been written to '{filename}'.")
        else:
            print("The sentence is not a question. It will not be saved.")

    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    filename = 'q6.txt'
    question_to_file(filename)


if __name__ == "__main__":
    main()
