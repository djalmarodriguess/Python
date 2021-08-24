x = (1, 2, 3)
#del(x[1]) #fails
#x[1] = 8  #fails
print(x)

y = ([1, 2], 3) # first value is a list
del(y[0][1])   # delete number 2, [0] = first value the tuple, [1] number position of list
print(y)


y = ([1, 2, 3, 4], 3) # first value is a list
del(y[0][3])   # delete number 4, [0] = first value the tuple, [3] number position of list
print(y)

y += (11,)
print(y)