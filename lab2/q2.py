def vowel_or_consonant(input_string):
    # Ensure the input string is not empty
    if not input_string:
        return "The input string is empty."

    # Convert the input string to lowercase for consistent checking
    input_string = input_string.lower()

    # Define vowels
    vowels = "aeiou"
    
    # Get the last letter of the string
    last_letter = input_string[-1]
    
    # Check if the last letter is a vowel or consonant
    if last_letter in vowels:
        return f"The last letter '{last_letter}' is a vowel."
    elif last_letter.isalpha():  # Ensure it's a letter
        return f"The last letter '{last_letter}' is a consonant."
    else:
        return "The last character is not a letter."

# Example usage
user_input = input("Enter a string: ")
print(vowel_or_consonant(user_input))
