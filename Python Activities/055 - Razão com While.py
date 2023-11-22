primeiro = int(input('Primeiro termo:'))
razão = int(input('razão:'))
contador = 1
termo = primeiro
while contador <= 10:
    print('{} '.format(termo), end='')
    termo = termo + razão
    contador = contador + 1
