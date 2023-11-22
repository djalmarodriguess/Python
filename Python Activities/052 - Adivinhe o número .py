from random import randint
soma = 1
print('''PENSE EM UM NÚMERO DE 0 A 10 
E TENTE DESCOBRIR QUAL O NÚMERO QUE O COMPUTADOR ESTÁ PENSANDO.''')
computador = int(randint(0, 11))
print('====' * 15)
jogador = int(input('Digite um número para saber se acertou: '))
print('====' * 10)
while jogador != computador:
    jogador = int(input('NÚMERO ERRADO, digite outro número: '))
    soma = soma + 1
    print('====' * 10)
print('PARABÉNS... VOCÊ ACERTOU na {}º tentativa.'.format(soma))
