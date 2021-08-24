from time import sleep
def contador(i, f , p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p < 0 :
        p *= -1
    if p == 0:
        p = 1
    cont = i
    if cont <= f:
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont += p
        print()
    else:
        while cont >= f:
            print(cont, end=' ')
            sleep(0.3)
            cont -= p
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora sua vez de personalizar a contagem')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
sleep(0.3)
contador(ini, fim, pas)

