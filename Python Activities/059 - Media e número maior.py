resposta = 'Ss'
contador = soma = media = maior = menor = 0
while resposta in 'Ss':
    n1 = int(input('Digite um número:'))
    soma = soma + n1
    contador = contador + 1
    if contador == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    resposta = str(input('Você que continuar? [S/N]:')).strip().upper()[0]
media = soma / contador
print('Fim, media {} numeros {}'.format(media, contador))
print('{} maior menor {}'.format(maior, menor))