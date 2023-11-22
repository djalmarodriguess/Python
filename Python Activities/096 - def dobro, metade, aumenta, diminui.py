def dobro(n):
    p = n * 2
    return p


def metade(n):
    p = n/2
    return p


def aumenta(n):
    p = n * 1.10
    return p


def diminui(n):
    p = n * 0.87
    return p


p = int(input('Digite um valor: R$'))
print(f'O dobro de {p} é {dobro(p)}')
print(f'A metade de {p} é {metade(p)}')
print(f'Aumentando de 10% no valor de {p} fica {aumenta(p)}')
print(f'Diminuindo 13% no valor de {p} fica {diminui(p)}')
