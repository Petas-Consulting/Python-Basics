'''
Tuple

Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
'''

mytuple = ("apple", "banana", "cherry")
print(mytuple)

'''
Tuple Items

Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
Ordered

When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
Unchangeable

Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
Allow Duplicates

Since tuples are indexed, they can have items with the same value:
Example

Tuples allow duplicate values:
'''
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#Print the second item in the tuple:
print(thistuple[1])
# Note: The first item has index 0.

#Print the last item in the tuple:
print(thistuple[-1])

# Return the third, fourth, and fifth item:
print(thistuple[2:5])

# This example returns the items from index -4 (included) to index -1 (excluded)
print(thistuple[-4:-1])
