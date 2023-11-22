num = (int(input('Digite o primeiro número: ')),int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')),int(input('Digite o quarto número: ')))
print(f'Os números digitados foram {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'Primeiro valor 3 na posição {num.index(3)+1}')
else:
    print('Não tem número 3')
print(f'Os número pares são: ',end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
