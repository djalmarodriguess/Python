n1 = int(input('Qual o primeiro número?'))
n2 = int(input('Qual o segundo número?'))
if n1 > n2:
    print('O número {} é maior que o {}'.format(n1, n2))
elif n1 == n2:
    print('Os dois valores são iguais')
else:
    print(" O número {} é maior que o número {}".format(n2, n1))