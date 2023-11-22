total = produto1000 = maisbarato = contador = 0
nomenovo = ' '
while True:
    nome = str(input(('Nome do Produto:')))
    preço = float(input('Preço: R$'))
    contador += 1
    if contador == 1:
        maisbarato = preço
        nomenovo = nome
    else:
        if preço < maisbarato:
            maisbarato = preço
            nomenovo = nome
    total = total + preço
    if preço > 1000:
        produto1000 += 1
    confirmação = ' '
    while confirmação not in 'SN':
        confirmação = str(input('Quer continuar?')).strip().upper()[0]
    if confirmação == 'N':
        break
print('-------------- FIM DE PROGRAMA ----------------')
print(f'O total da compra foi: R${total}')
print(f'Temos {produto1000} custando mais de R$1000,00.')
print(f'O produto mais barato foi {nomenovo} que custa {maisbarato}')


