from moeda import aumenta, diminui, dobro,metade
p = int(input('Digite um valor: R$'))
print(f'O dobro de {p} é {dobro(p)}')
print(f'A metade de {p} é {metade(p)}')
print(f'Aumentando 10% no valor de {p} fica {aumenta(p)}')
print(f'Diminuindo 13% no valor de {p} fica {diminui(p)}')