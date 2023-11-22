num = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor %2 == 0:
        num[1].append(valor)
    else :
        num[0].append(valor)
num[1].sort()
num[0].sort()
print(f'Todos os valores são {num}')
print(f'Os valores pares são {num[1]}')
print(f'Os valores impares são {num[0]}')