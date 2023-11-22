cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez')
while True:
    num = int(input('Digite um numero de 0 a 10:'))
    while num < 0 or num >10:
        num = int(input('Número invalido, Digite um numero de 0 a 10:'))
    print(f'Você digitou o número {cont[num]}.')
    confirmação = ' '
    while confirmação not in 'SN':
        print('~~' * 20)
        confirmação = str(input('Deseja continuar?[S/N]:')).strip().upper()[0]
    if confirmação in 'N':
        break
print("FIM DE PROGRAMA")



