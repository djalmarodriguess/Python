primeiro = int(input('Primeiro termo:'))
razão = int(input('razão:'))
contador = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} '.format(termo), end='')
        termo = termo + razão
        contador = contador + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ?'))
    print('-=-'*20)
print('Progressão terminada com {} termos mostrados'.format(total))