'''
Upper Case
Example
The upper() method returns the string in upper case:
'''
a = "Hello, World!"
print(a.upper())

print("==========================")

'''Lower Case
Example
The lower() method returns the string in lower case:
'''
a = "Hello, World!"
print(a.lower())

print("=======================")
'''
Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

Example
The strip() method removes any whitespace from the beginning or the end:
'''
a = " Hello, World! "
print(a)
print(a.strip()) # returns "Hello, World!"

print("=======================================")
'''
Replace String
Example
The replace() method replaces a string with another string:
'''
a = "Hello, World!"
print(a.replace("H", "J"))

print("================================")
'''
Split String
The split() method returns a list where the text between the specified separator becomes the list items.

Example
The split() method splits the string into substrings if it finds instances of the separator:
'''
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

print("==================================")
'''Example
Return the number of times the value "apple" appears in the string:

'''
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)
