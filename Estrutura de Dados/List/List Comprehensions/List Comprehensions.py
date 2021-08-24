import random


#get values within range
under_10 = [ x for x in range(10)]
print(f'under 10: {under_10}')


#get square values
squares = [ x**2 for x in range(10)]
print(f'squares: {squares}')
#or
squares_1 = [ x**2 for x in under_10]
print(f'squares_1: {squares_1}')


#get odd numbers using mod
odds= [ x for x in range(10) if x % 2 == 1]
print(f'odd: {odds}')


#get multiples of 10
multiple_10= [ x * 10 for x in range(1, 10)]
print(f'multiples 10: {multiple_10}')


# get all numbers from a string
s = '2hjg8jkb9o0'
num = [x for x in s if x.isnumeric()]
print('numbers:' + ''.join(num))


#get index of a list
names = ['Ana', 'Maria', 'Carlos', 'Dani']
idx = [k for k, v in enumerate(names) if v == 'Carlos']
print('index: ' + str(idx[0]))


#delete a item from a list
letters = [x for x in 'ABCDEF']
random.shuffle(letters)
new = [y for y in letters if y != 'C']
print(letters, new)


#if-else condition in a comprehension
num = [5, 3, 6, 10 , 8, 11, 4, 6]
new_num = [x if x % 2 == 0 else 10*x for x in num ]
print(new_num)


#nested loop iteration for 2D list
a = [[1, 2], [3, 4]]
new_list = [x for b in a for x in b]
print(new_list)
