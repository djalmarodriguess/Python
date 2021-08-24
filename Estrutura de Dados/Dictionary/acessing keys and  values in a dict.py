x = {'pork':26.70, 'beef':20.30, 'chicken':12.99}
print(x.keys())
print(x.values())
print(x.items())

#Outra forma de vizualizar as keys individualmente.
for i in x.keys():
    print(i)

print()
#check a specific membership in x.key
print('pork' in x) #only looks in keys, not in values, don't need specific "x.keys()".
                    # Return values booleans

#check a specific membership in x.value
print( 12.99 in x.values()) # Here needs specific "x.values()".
                            #Return values booleans