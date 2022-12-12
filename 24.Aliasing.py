x = [71, 72, 73]
y = [71, 72, 73]

print(x is y) #False
print("=================")
y = x
print(x is y) # True
print(x == y)  # True

print("=================")

y[0] = 5
print(x)
