contador = 0
num = int(input('Digite um numero:'))
for c in range(1, num+1):
    print((c), end=' ')
    if num % c == 0:
        contador = contador + 1
print('\nO número {} foi dividido {} veses.'.format(num, contador))
if contador == 2:
    print('O valor {} É PRIMO'. format(num))
else:
    print('O valor {} NÃO É PRIMO.'.format(num))
