somaidade = somahomem = somamulheres20 = 0
while True:
    idade = int(input('Qual a idade?'))
    sexo = ' '
    confirmação = ' '
    if idade > 18:
        somaidade = somaidade + 1
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo? [M/F]')).strip().upper()
        if sexo == 'M':
            somahomem = somahomem + 1
        elif sexo == 'F' and idade < 20:
            somamulheres20 = somamulheres20 + 1
    while confirmação not in 'SN':
        confirmação = str(input('Quer continuar?')).strip().upper()[0]
    if confirmação == 'N':
        break
    print('~~~~' * 10)
print(f'Foram cadastrados {somahomem} homens.')
print(f'{somaidade} pessoas tem mais de 18 anos')
print(f'{somamulheres20} mulheres tem menos de 20 anos')
print('Acabou')





