def maior(*num):
    print(f'Analisando os valores passados.. ')
    cont = maior = 0
    for valor in num:
        print(valor, end=' ')
        if cont == 0:
            maior = valor
            cont += 1
        else:
            if valor > maior:
                maior = valor
            cont += 1

    print(f'\nForam lidos {cont} números e o maior é {maior}')
    print('~~'*30)


maior(1, 2, 3, 4, 5, 6, 7)
maior(0, 11, 6 , 3)
maior(12, 3, 10)
maior()
