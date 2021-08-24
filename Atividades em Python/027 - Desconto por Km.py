km = int(input("Quantos Km?"))
menorkm = km * 0.5
maiorkm = km * 0.45
if km <= 200:
    print('Resultado é {:.2f}'.format(menorkm))
else:
    print('Resultado é {:.2f}'.format(maiorkm))