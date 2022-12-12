s = 5
p = "5"
# please note s and p are not the same
# s is an integer while p is a sting
print(type(s))
print(type(p))

print("=============================================================")
#let try simple addition operations on this datatypes

print(s + 5)
#print(p + 5) this will raise an error because python can not add string with integer
print("=============================================================")
# we noticed we have an error when adding p with 5, python cannot add a int and str together

                            # String Slicing
'''Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Example
Get the characters from position 2 to position 5 (not included):
'''
b = "Hello, World!"
print(b[2:5])
# Note: The first character has index 0.
print("=============================================================")
'''
By leaving out the end index, the range will go to the end:

Example
Get the characters from position 2, and all the way to the end:
'''
b = "Hello, World!"
print(b[2:])
print("==========================================================")

'''
Use negative indexes to start the slice from the end of the string:
Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
'''
b = "Hello, World!"
print(b[-5:-2])

