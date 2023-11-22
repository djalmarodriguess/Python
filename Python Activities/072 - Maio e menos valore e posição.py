valores = []
maior = menor = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um número para posição {v}:')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'O maior número é o {maior} e sua posição é ', end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}...', end='')
print()
print(f'O menor número é o {menor} e sua posição é ', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}...', end='')
print()
