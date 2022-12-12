a = "banana"
b = "banana"
print(id(a))
print(id(b))
print(a is b) # the value of a is also the value for b using the id so we will have a True
print("====================================")
a = "banana"
b = "orange"
print(a is b) # the value of a is not the value for b so we will have a False

print("====================================")
x = [71, 72, 73]
y = [71, 72, 73]

print(x is y) # we will have a False because the id of x and y are different
print(x == y) # we will have a true because the values of x = to the value of y


print(id(x))
print(id(y))
