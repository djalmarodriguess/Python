casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual seu salário?'))
anos = int(input('Em quantos pretender pagar?'))
prestação = casa / (anos * 12)
print('O valor da casa de R${:.2f}, financiada em {} anos a pretação será de {:.2f},'.format(casa, anos, prestação), end='')
if prestação <= salario * 0.3:
    print('vai dar para fazer o financiamento.')
else:
    print('não vai dar para fazer o financiamento.')
