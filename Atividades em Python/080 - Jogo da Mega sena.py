from random import sample
from time import sleep
jogo = []
n = int(input('Quantos jogos você deseja? '))
for c in range(n):
    a = sorted(sample(range(1, 61), 6))
    jogo.append(a[:])
    print(f'Jogo {c+1}: {a}')
    sleep(1)
