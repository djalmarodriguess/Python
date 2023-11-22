matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somacoluna = somalinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um numero para posição [{l},{c}]: ')))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    print()
print(f'A soma dos valores pares é {soma}.')
for c in range(0, 3):
    somacoluna+=matriz[c][2]
print(f'A soma da terceira coluna é {somacoluna}')
for l in range(0, 3):
    somalinha+=matriz[1][l]
print(f'A soma da segunda linha é {somalinha}')
