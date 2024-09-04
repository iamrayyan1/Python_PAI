def question_to_file(filename):

    try:

        sentence = input("Enter a sentence: ").strip()

        # Check if the sentence is a question
        if sentence.endswith('?'):
            with open(filename, 'w') as file:
                file.write(sentence + '\n')
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
