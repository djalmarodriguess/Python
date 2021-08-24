n = int(input('Quantos termos você quer mostrar? '))
print('~~'*30)
t1 = 0
t2 = 1
print('{} {} '.format(t1, t2), end='')
contador = 2
while contador != n:
    t3 = t1 + t2
    print(' {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1


