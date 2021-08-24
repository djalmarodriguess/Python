valores = []
while True:
    n = (int(input('Digite um número:')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, Não adicionado...')
    p = str(input('Quer continuar?[S/N]:')).strip().upper()[0]
    print('=+=' * 30)
    while p not in 'NS':
        p = str(input('Somente permitido Sim ou Não?[S/N]:')).strip().upper()[0]
    if p in 'N':
        break
valores.sort()
print(f'Os valores são {valores}')


