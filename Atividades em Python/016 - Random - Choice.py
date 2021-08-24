from random import choice
a1 = str(input('Aluno1:'))
a2 = str(input('Aluno2:'))
a3 = str(input('Aluno3:'))
a4 = str(input('Aluno4'))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('Sorteado é {}'. format(escolhido))