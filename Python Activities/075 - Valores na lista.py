valores = []
par = []
impar = []
while True:
    n = (int(input('Digite um número:')))
    valores.append(n)
    r = str(input('Quer continuar?'))
    if n % 2 == 0:
        par.append(n)
    elif n% 2 == 1:
        impar.append(n)
    if r in 'Nn':
        break
print(f'Os valores são {valores}')
print(f'Números pares sao = {par}')
print(f'Números impares são = {impar}')