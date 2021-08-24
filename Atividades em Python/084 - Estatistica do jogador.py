dados = {}
total = 0
dados['Jogador'] = str(input('Nome do jogador: '))
dados['Partidas'] = int(input(f'Quantas partidas {dados["Jogador"]} jogou? '))
if dados['Partidas'] != 0:
    for c in range(dados['Partidas']):
        dados['gol'] = int(input(f'Quantos gols no {c+1}º jogo?'))
        total += dados['gol']
    print('-='*40)
    print(f'Jogador {dados["Jogador"]} jogou {dados["Partidas"]} partidas e fez {total} gols.')
    print('-='*40)

