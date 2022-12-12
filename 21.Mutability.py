'''
Python mutability means an object's ability to change.
An immutable object cannot change, but a mutable object can.
For example, a list is mutable, but a tuple is not.
In other words, you can freely change the elements of a list, but not the ones of a tuple.
'''

'''
Change Item Value
To change the value of a specific item, refer to the index number:

Example
Change the second item:
'''
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

print("=========================================")
'''
Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

Example
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] # index [1:3] means the second item to the third item in the list
print(thislist)

print("=========================================")
'''
If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

Example
Change the second value by replacing it with two new values:
'''
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] # index [1:2] means the sencond item in the list only
print(thislist)

print("=========================================")
'''
Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.
The insert() method inserts an item at the specified index:

Example
Insert "watermelon" as the third item:
'''
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

print("==================================")
greet = ("Hello World!")
newgreet = 'J' + greet[1:]
print(newgreet)
print(greet)
