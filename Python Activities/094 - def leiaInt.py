def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO, valido somente números')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'O numero é {n}')
