compra = float(input('Qual preço da compra? R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual a opção?'))
if opção == 1:
    total = compra * 0.9
elif opção == 2:
    total = compra * 0.95
elif opção == 3:
    total = compra
    print('Sua compra de R${:.2f} será parcelada em 2x R${:.2f}'.format(compra, compra/2))
elif opção == 4:
    total = compra * 1.2
    parcelas = int(input('Quantas parcelas?'))
    totalparc = total/parcelas
    diferença = total - compra
    print('Sua compra será parcelada em {}x de {:.2f} , juros de R$ {:.2f}'.format(parcelas, totalparc, diferença))
else:
    print("OPÇÃO INVÁLIDA")
print('Sua compra de R${:.2f} vai custar {:.2f}'.format(compra, total ))




