aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Media do {aluno["Nome"]} é : '))
if aluno['Média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprocado'
for k,v in aluno.items():
    print(f'{k} é igual a {v}')