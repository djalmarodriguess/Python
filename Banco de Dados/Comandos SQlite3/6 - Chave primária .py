import sqlite3

cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes (nome text, sobrenome text, email text)" )

'''Consultar o banco de dados e colocar o numero de identifição em cada linha
   Isso vai facilitar na edição dos dados, pois pode-se modificar a partir desse número inserido
   Entrar com o comando "rowid,"'''
cursor.execute("SELECT rowid, * FROM clientes")
registros = cursor.fetchall()

for clientes in registros :
    print(clientes)

cliente.commit()
cliente.close()



