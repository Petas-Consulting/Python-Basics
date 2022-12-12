#           Python For Loops
'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
'''
#Example:   Print each fruit in a fruit list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# The for loop does not require an indexing variable to set beforehand.

print("================================================================")

#           Looping Through a String

#Even strings are iterable objects, they contain a sequence of characters:
#Example:    Loop through the letters in the word "banana":
for x in "banana":
  print(x)

print("================================================================")

#           The break Statement
#With the break statement we can stop the loop before it has looped through all the items:
#Example:    Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry","mango"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print("================================================================")

#           The continue Statement
#With the continue statement we can stop the current iteration of the loop, and continue with the next:
#Example:   Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("================================================================")



#               Else in For Loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
#Example:   Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#Note: The else block will NOT be executed if the loop is stopped by a break statement.
print("================================================================")

#Example:  Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
