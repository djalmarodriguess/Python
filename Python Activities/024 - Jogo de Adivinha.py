from random import randint
from time import sleep
computador = (randint(0, 5))
print('==*==' * 20)
print('Tente adivinhar, vou pensar em um número de 0 a 5...')
print('==*==' * 20)
jogador = int(input('Que número eu pensei?'))
print('PROCESSANDO....')
sleep(1.5)
if jogador == computador:
    print('PARABÉNS!!!...Você venceu')
else:
    print('Computador venceu, o número que pensei foi {} não o {}'.format(computador, jogador))
