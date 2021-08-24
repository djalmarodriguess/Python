def ficha(nome='<desconhecido>', gols=0):
    print(f'O nome do jogador é {nome} e fez {gols} gols no campeonato')


n = str(input('Qual o nome do jogador: '))
g = str(input('Quantos gols ele fez: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)