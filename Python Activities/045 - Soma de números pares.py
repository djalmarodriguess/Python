soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite um valor:'))
    if num % 2 == 0:
        soma = soma + num
        cont = cont +1
print('{} números são pares e a soma total é deles é {}'.format(cont, soma))
