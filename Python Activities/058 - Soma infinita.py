contador = 0
soma = 0
n1 = int(input('Digite um número:'))
while n1 != 999:
    contador += 1
    soma = soma + n1
    n1 = int(input('Digite um número:'))
print('Você digitou {} número e a soma entre ele é {}'.format(contador, soma))

