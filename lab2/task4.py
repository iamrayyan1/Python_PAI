def show_info(**details):
    output = ""
    for key in details:
        output += key + ": " + str(details[key]) + "\n"
    return output

# Call the function and print the result
print(show_info(name="Rija Ali", age=20))
