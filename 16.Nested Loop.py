#           Nested Loops
'''
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":
'''
#Example:  Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

print("================================================================")

#       The pass Statement
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
#Example
for x in [0, 1, 2]:
  pass
