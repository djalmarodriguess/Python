pessoa = dict()
galera = list()
idade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo:[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO,somente [M/F]: ')
    pessoa['idade'] = int(input('Qual a idade? '))
    idade = idade + pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Quer continuar?[S/N]: ')).upper()[0]
        if r in 'SN':
            break
        print('ERROR, SOMENTE [S/N]: ')
    if r == "N":
        break
print('-='*50)
print(f'A) {len(galera)} pessoas cadastradas.')
media = idade/len(galera)
print(f'B) A idade média das pessoa é {media} anos')
print(f'C) As mulheres cadastradas são ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print('\nD) As pessoas acima da média são ', end='')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]} ', end='')
print()

