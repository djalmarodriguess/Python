a = input('Digite um valor:')
b = input('Digite um valor:')
c = input('Digite um valor:')
# Verificando o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificar o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('Maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))