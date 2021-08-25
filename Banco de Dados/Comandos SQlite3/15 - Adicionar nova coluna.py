import sqlite3

cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()


''' Adicionando uma nova coluna na tabela clientes'''
cursor.execute("ALTER TABLE clientes ADD COLUMN idade INTEGER")

cliente.commit()

print('Novo campo adicionado com sucesso.')

cliente.close()