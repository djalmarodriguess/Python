sexo = str(input('Qual o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos: Por favor informe o seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso:'.format(sexo))

