#Listas para armazenamento de dados 
dados_aluno = []
todas_medias = []
acima_media = []
abaixo_media = []
# igual_media = []

for i in range (2):
    print(f'Aluno {i+1}')
    aluno = f'Aluno {i+1}'
    nota1 = float(input('1º Nota: '))
    nota2 = float(input('2º Nota: '))
    nota3 = float(input('3º Nota: '))

    print('='*40)

    media = (nota1+nota2+nota3)/3
    dados_aluno.append([aluno,[nota1,nota2,nota3], media]) 
    todas_medias.append(media)



#Nota final de cada aluno
for p in dados_aluno:
    print(f'Nota final do {p[0]} = {p[2]:.2f} pontos')

print('='*40)

#Média geral de todas as notas
media_geral = (sum(todas_medias))/len(todas_medias)
print(f'Media Geral = {media_geral:.2f}')

# Verificação e separação das notas maiores do que a média geral.
for i in dados_aluno:
    if i[2] > media_geral:
        acima_media.append(i[2])
    else:
        abaixo_media.append(i[2])

print('='*40)

# Quantidade de alunos que obtiveram nota acima da média;
if len(acima_media) > 1:
    print(f'{len(acima_media)} alunos tiraram acima da média geral')
else:
    print(f'Apenas {len(acima_media)} aluno tirou nota acima da média geral')

print('='*40)

# Quantidade de alunos que obtiveram nota abaixo da média.
if len(abaixo_media) > 1:
    print(f'{len(abaixo_media)} alunos tiraram abaixo da média geral')
else:
    print(f'Apenas {len(abaixo_media)} aluno tirou nota abaixo da média geral')

print('='*40)