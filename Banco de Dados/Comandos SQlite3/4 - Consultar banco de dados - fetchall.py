import sqlite3

cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes (nome text, sobrenome text, email text)" )


'''Consultar o banco de dados'''
cursor.execute("SELECT * FROM clientes")

'''Temos três tipos de buscas
#cursor.fetchone()   #retorna apenas o ultimo item da tabela
#cursor.fetchmany(3) #retorna varios itens na lista ao mesmo tempo.EX: solicitei (3), aparecerá apenas os 3 primeiros usuarios na tabela.
#cursor.fetchall()   #retorna todos cadastrados na lista'''

print(cursor.fetchall())

cliente.commit()
cliente.close()



