from random import randint
soma = 0
while True:
    jogador = int(input('Diga um valor:'))
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('Par ou impar? [P/I]:')).strip().upper()[0]
    computador = randint(0, 11)
    total = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}. Total é {total}')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você venceu.')
            soma+= 1
        else:
            print('Você perdeu.')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você venveu.')
            soma+=1
        else:
            print('Você perdeu')
            break
print(f'Gamer over, você venceu {soma}')


