palavras = ('estudar', 'Python', 'divertido', 'programação',
            'aulas', 'curso', 'trabalhar', 'profissional',
            'aprender', 'crescer', 'evoluir', 'game')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')