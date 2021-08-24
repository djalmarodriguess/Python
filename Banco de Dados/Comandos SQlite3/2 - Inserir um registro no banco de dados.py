import sqlite3

cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes (nome text, sobrenome text, email text)" )

'''Inserindo um novo registro no banco, de forma manual.'''
cursor.execute("INSERT INTO clientes VALUES ('José', 'Nunes', 'jose@hotmail.com')")

print('Cliente registrado com sucesso')


cliente.commit()
cliente.close()



