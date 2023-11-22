while True:
    d = int(input('Você deseja a tabuada de qual número?'))
    print('~~' * 20)
    if d < 0:
        break
    for c in range(0, 11):
        print('{} x {} = {}'.format(c, d, c * d))
    print('~~' * 20)
print('PROGRAMA FINALIZADO')


