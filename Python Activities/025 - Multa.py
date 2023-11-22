v = float(input('Velocidade:'))
m = (v-80)*7
if v > 80:
    print('Voce foi multado por excesso de velocidade, sua multa é de R${:.2f} reais'.format(m))
    print('Boa viagem, e cuidado')
else:
    print('Boa viagem')