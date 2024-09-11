# Suppose a = ["He", "th", "i", "sal"] and b = ["llo", "is", "s", "man"]
# You need to print this : ['Hello', 'this', 'is', 'salman']

# Name: Rija Ali
# ID: 23k-0057



a = ["He" , "th" , "i" , "sal"]
b = ["llo", "is", "s", "man"]

output = [x+y for x,y in zip(a,b)]

print(output)
