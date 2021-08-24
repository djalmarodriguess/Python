maisvelho = 0
maisnovo = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for c in range(1, 4):
    print('----- {}º PESSOA -----'.format(c))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade = somaidade + idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totalmulher20 + 1
print('media {} anos:'.format(somaidade/c))
print(f'O homem mais velho tem {maioridadehomem} anos e seu nome é {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')

