from datetime import date
ano = date.today().year
contador1 = 0
contador2 = 0
for pessoas in range(1, 8):
    nascimento = int(input('Em que ano a {}º pessoa nasceu:'.format(pessoas)))
    idade = ano - nascimento
    if idade >= 18:
        contador1 = contador1 + 1
    else:
        contador2 = contador2 + 1
print('Das 7 pessoas {} são maiores de idade.'.format(contador1))
print('E {} pessoas são menores de idade.'.format(contador2))


