'''
In Python, use list methods clear() , pop() , and remove() to remove items (elements) from a list.
It is also possible to delete items using del statement by specifying a position or range with an index or slice.
'''
'''
The remove() method removes the specified item.

Example
Remove "banana":
'''
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

print("=========================================")

'''The pop() method removes the specified index.

Example
Remove the second item:
'''
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # index 1 is the second item on the list
print(thislist)
print("====================================================")
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
print("===============================================")

'''The del keyword also removes the specified index:

Example
Remove the first item:
'''
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
'''
print("===============================================")
The del keyword can also delete the list completely.

Example
Delete the entire list:
'''
thislist = ["apple", "banana", "cherry"]
del thislist

print("===============================================")
'''
The clear() method empties the list.

The list still remains, but it has no content.

Example
Clear the list content:
'''
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # we will have an error because all item on the list have been deleted and the list does not exist anymore

