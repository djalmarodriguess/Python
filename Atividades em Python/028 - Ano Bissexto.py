from datetime import date
ano = int(input('Digite um ano, e se quiser saber se o ano atual é bissexto digite 0:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é Bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))