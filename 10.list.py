'''
        List
Lists are used to store multiple items in a single variable.
'''
mylist = ["apple", 100 , "banana", 68 , "cherry"]
print(mylist)


'''
List Items

List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.
Ordered

When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of the items will not change.
Changeable

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
Allow Duplicates

Since lists are indexed, lists can have items with the same value:
'''

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
'''
List Length

To determine how many items a list has, use the len() function:
Example

Print the number of items in the list:
'''

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

'''
A list can contain different data types:
Example

A list with strings, integers and boolean values:
'''
list1 = ["abc", 34, True, 40, "male"]
print(list1)


'''
The list() Constructor

It is also possible to use the list() constructor when creating a new list.
Example

Using the list() constructor to make a List:
'''
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


'''
Access Items

List items are indexed and you can access them by referring to the index number:
Example

Print the second item of the list:
'''

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Print the last item of the list:
print(thislist[-1])

# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
