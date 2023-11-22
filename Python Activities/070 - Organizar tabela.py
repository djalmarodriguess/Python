
prod= ('lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
            'estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            'mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)
for c in range(0, len(prod), 2):
    print(f'{prod[c]:.<30}R${prod[c + 1]:7.2f}')
