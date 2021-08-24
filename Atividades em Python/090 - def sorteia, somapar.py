from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista...')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(c, end=' ')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nA soma dos valores pares da lista, {lista}, é de {soma} ')


numeros = list()
sorteia(numeros)
somapar(numeros)


