n = (int(input('1º numero: ')), int(input('2º numero: ')), int(input('3º numero: ')),
     int(input('6º numero: ')), int(input('5º numero: ')))
print('=='*30)
print(f'O número 9 aparece {n.count(9)}')
print('=='*30)
if n == 3:
    print(f'O primeiro 3 foi digitado na posição {n.index(3)+1}')
else:
    print('Não tem numero 3.')
print('=='*30)
print(f'Os números pares são: ')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')


