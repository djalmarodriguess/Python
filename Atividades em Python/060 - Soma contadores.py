soma = contador =  0
while True:
    c = int(input('Digite um número:'))
    if c == 999:
        break
    soma = soma + c
    contador = contador + 1
print(f'A soma dos {contador} numeros é {soma} ')

