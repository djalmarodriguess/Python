import time
from random import randint
from time import sleep
print('=*='* 12)
print('Está preparado para perder?!!')
print('=*='* 12)
itens = (' ', 'Pedra', 'Papel', 'Tesoura')
computador = randint(1, 3)
print('''Suas opções
[ 1 ] PEDRA
[ 2 ] PAPEL 
[ 3 ] TESOURA''')
jogador = int(input('Qual a sua esolha?'))
print('=*=' * 12)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)
print('=*=' * 12)
print(' O Computador jogou {}'.format(itens[computador]))
print(' O Jogador jogou {}'.format(itens[jogador]))
print('=*=' * 12)
# COMPUTADOR É PEDRA
if computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    elif jogador == 3:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDO')
# COMPUTADOR É PAPEL
elif computador == 2:
    if jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDO')
 #COMPUTADOR É TESOURA
elif computador == 3:
    if jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    elif jogador == 3:
        print('EMPATE')
    else:
        print('JOGADA INVALIDO')










