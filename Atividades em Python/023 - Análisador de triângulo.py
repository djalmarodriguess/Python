print('-=-' *20)
print('Análisador de triângulo')
print('-=-' * 20)
a = int(input('Digite o primeiro lado do triângulo:'))
b = int(input('Digite o segundo lado do triângulo:'))
c = int(input('Digite o terceiro lado do triângulo:'))
if a < b + c and b < a + c and c < a + b:
    print('É um triangulo')
else:
    print('Não é um triangulo')