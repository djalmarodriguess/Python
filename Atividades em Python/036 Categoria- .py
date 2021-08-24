from datetime import date
ano = int(input('Ano de nacimento:'))
idade = date.today().year - ano
if idade > 20:
    print('O atleta tem {} anos\nCaregoria: MASTER'.format(idade))
elif idade <= 9:
    print('O atleta tem {} anos\nCaregoria: MIRIM'.format(idade))
elif 9 < idade <=14:
    print('O atleta tem {} anos\nCaregoria: INFANTIL'.format(idade))
elif 14 < idade <= 19:
    print('O atleta tem {} anos\nCaregoria: JUNIOR'.format(idade))
elif 19 < idade <= 20:
    print('O atleta tem {} anos\nCaregoria: SÊNIOR'.format(idade))
