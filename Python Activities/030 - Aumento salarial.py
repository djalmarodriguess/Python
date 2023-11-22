salario = float(input('Digite o salário: R$'))
if salario > 1250:
    print("Seu novo salário é de {:.2f}".format(salario*1.1))
else:
    print('Seu novo salário é de {:.2f}'.format(salario*1.15))