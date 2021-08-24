#add or update
x = {'pork':26.70, 'beef':20.30, 'chicken':12.99}
x['fish'] = 10.7
print(x)

#delete a item
del(x['pork'])
print(x)

#get length
print(len(x))

#delete all items from dict
x.clear()
print(x)

#delete dict x
del(x)
