valores = []
while True:
    n = int(input('Digite um número:'))
    valores.append(n)
    r = ' '
    while r not in 'NS':
        r = str(input('Quer continuar:[S/N]:')).strip().upper()[0]
    if r in 'nN':
        break
print(f'Foram digitados {len(valores)} valores')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescentes são {valores}')
if 5 in valores:
    print('O valor 5 está na lista.')
else:
    print('Não tem número 5 na lista.')