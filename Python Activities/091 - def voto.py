def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com a idade de {idade} anos É PROIBIDO VOTAR'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com a idade de {idade} anos o voto É OPCIONAL'
    else:
        return f'Com a idade de {idade} anos o voto é OBRIGATÓRIO'


a = int(input('Qual o ano de nascimento: '))
print(voto(a))

