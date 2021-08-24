# Python Program to get the first digit of number

# importing math module
import math 

# take input
num = int(input('Enter any Number: '))

# get the first digit
digits = int(math.log10(num))
first_digit = int(num / pow(10, digits))

# printing first digit of number
print('The first digit of number:', first_digit)