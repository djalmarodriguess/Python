lista = []
n = []
maior = menor = 0
while True:
    n.append(str(input('Nome: ')))
    n.append(int(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = n[1]
    else:
        if n[1] > maior:
            maior = n[1]
        if n[1] < menor:
            menor = n[1]
    lista.append(n[:])
    n.clear()
    r = str(input('Quer continuar?[S/N]: '))
    if r in 'Nn':
        break
print(f' Valores dos dados {lista}')
print(f'Total cadatrados na lista {len(lista)}')
print(f'maior peso {maior}kg')
print(f'menor peso {menor}kg')