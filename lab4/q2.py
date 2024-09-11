# Two lists are given : list1 = ["Hello ", "take "] , list2 = ["Dear", "Sir"]
# Concatenate these two lists like this : ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

output1 = [x+y for x in list1 for y in list2 ]
# output2 = [x+y for x,y in zip(list1,list2)]

print(output1)
# print(output2)
