from time import sleep
v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))
escolha = 0
while escolha != 5:
    print('''
[ 1 ] Somar 
[ 2 ] Multiplicar 
[ 3 ] Maior
[ 4 ] Novos Nùmeros
[ 5 ] Sair do Programa''')
    escolha = int(input('>>>>>Qual a sua escolha? <<<<<'))
    if escolha == 1:
        soma = v1 + v2
        print('A soma de {} + {} = {}'.format(v1, v2, soma))
    elif escolha == 2:
        mult = v1 * v2
        print('A multiplicação de {} * {} = {} '.format(v1, v2, mult))
    elif escolha == 3:
        if v1 > v2:
            print('O numero {} é maior que {}.'.format(v1, v2))
        else:
            print('O numero {} é maior que {}.'.format(v2, v1))
    elif escolha == 4:
        print('Informe os valores novamente: ')
        v1 = float(input('Digite um valor: '))
        v2 = float(input('Digite outro valor: '))
    elif escolha == 5:
        print('Finalizando...')
        sleep(1.4)
    else:
        print('Opção invalida. Tente novamente.')
    print('-=-'*20)
print('FIM do PROGRAMA')


