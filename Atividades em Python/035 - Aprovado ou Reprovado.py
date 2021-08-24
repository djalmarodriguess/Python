nota1 = float(input("Primeira nota:"))
nota2 = float(input('Segunta nota:'))
media = (nota1 + nota2) / 2
if media > 7:
    print('Parabéns você está aprovada, a media das suas notas foram de {:.2f} pontos'.format(media))
elif media < 5:
    print('Sinto muito, não foi dessa vez, você foi REPROVADO, sua nota é de {:.2f} pontos,\nseria necessario no mínimo 7 pontos para aprovação'.format(media))
elif 5 <= media < 7:
    print('Você esta de RECUPERAÇÂO, sua note é de {:.2f},\nvocê precisa de no mínimo 7 pontos'.format(media))

