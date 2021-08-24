from random import randint
from operator import itemgetter
from time import sleep
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
rank = []
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse = True)
print('-='*30)
print('          ===RANKING===   ')
for i,v in enumerate(rank):
    print(f'   {i+1}º lugar : {v[0]} com {v[1]}')
    sleep(1)
