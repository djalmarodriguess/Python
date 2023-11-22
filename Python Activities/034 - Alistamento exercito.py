from datetime import date
ano = int(input('Ano de nascimento:'))
n = date.today().year - ano
print('Quem nascel em {} tem {} anos em {}'.format(ano, n, date.today().year))
if n == 18:
    print('Está na idade certa para fazer o alistamento')
elif n > 18:
    print('Você deveria ter se alistado a {} anos '.format(n - 18))
else:
    print('Ainda falta {} anos para se alistar'.format(18 - n))