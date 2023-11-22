pesomaior = 0
pesomenor = 0
for pessoa in range(1, 6):
    peso = float(input('Peso da {}º pessoa:'.format(pessoa)))
    if pessoa == 1:
        pesomenor = peso
        pesomaior = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print('O maior peso é {}kg'.format(pesomaior))
print('O menor peso é {}kg'.format(pesomenor))
