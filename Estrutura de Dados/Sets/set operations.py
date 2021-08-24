# Creating new sets
# Never repeat the same value
# Sort automatic the values


# add a new value
x = {1, 2, 3, 4}
print(x)
x.add(9)
print(x)

# remove a item
x.remove(3)  #remove number 3
print(x)

# length of set y
y = {1, 2, 3, 4, 4, 4, 4, 6}
print(len(y))

# check membership in y
print(6 in y)
print(5 in y)

# pop random item from set y
print(y.pop(), y)

#delete all items from set y
y.clear()
print(y)


