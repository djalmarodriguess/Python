from random import randint

while True:
    x = randint(1, 6)
    if x == 1:
        print('[---------]\n'
              '[         ]\n'
              '[    0    ]\n'
              '[         ]\n'
              '[---------]')
    elif x == 2:
        print('[---------]\n'
              '[      0  ]\n'
              '[         ]\n'
              '[  0      ]\n'
              '[---------]')
    elif x == 3:
        print('[---------]\n'
              '[      0  ]\n'
              '[    0    ]\n'
              '[  0      ]\n'
              '[---------]')
    elif x == 4:
        print('[---------]\n'
              '[ 0     0 ]\n'
              '[         ]\n'
              '[ 0     0 ]\n'
              '[---------]')
    elif x == 5:
        print('[---------]\n'
              '[ 0     0 ]\n'
              '[    0    ]\n'
              '[ 0     0 ]\n'
              '[---------]')
    elif x == 6:
        print('[---------]\n'
              '[ 0     0 ]\n'
              '[ 0     0 ]\n'
              '[ 0     0 ]\n'
              '[---------]')

    p = str(input('Quer jogar outra vez o dado? ')).upper()[0]
    while p not in 'SN':
        p = str(input('Somente Sim ou Não,[S/N]: ')).upper()[0]
    if p == 'N':
        print('Fim da jogada')
        break
