valor = int(input('Que valor você que sacar? R$'))
total = valor
cedula = 50
contadorcdula = 0
while True:
    if total >= cedula:
        total = total - cedula
        contadorcdula = contadorcdula + 1
    else:
        if contadorcdula > 0:
            print(f'Total de {contadorcdula} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contadorcdula = 0
        if total == 0:
            break