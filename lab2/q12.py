# Write a python program that takes any two lists from user having same number of
# elements. Make a dictionary from these two lists in such a way that first element of first list
# will be key and first element of second list will be its associated value and so on and print
# the result.
# Note: do not use any library. Make logic yourself.

#defining function
def lists(keys, values):
    dict = {}
    
    for i in range(len(keys)):
        dict[keys[i]] = values[i]
    return dict

keys = ["City" , "Province" , "Country"]
values = ["Karachi" , "Sindh" , "Pakistan"]

#checking if length of keys and value is same
if len(keys) != len(values):
    print("Error: The lists must have the same number of elements.")
else:
  
    output = lists(keys, values)
    
    # Printing the results
    print("The resulting dictionary is:")
    print(output)
