import sqlite3

cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes (nome text, sobrenome text, email text)" )


'''Consultar o banco de dados'''
cursor.execute("SELECT * FROM clientes")

'''Criar uma variavel'''
registros = cursor.fetchall()   #retorna todos cadastrados na lista


'''A tabela pode ser vista assim:'''
for clientes in registros :
    print(clientes)

'''Ou assim:'''
'''for clientes in registros :
    print(clientes[0] + '\t' + clientes[1] + '\t\t' + clientes[2])'''

cliente.commit()
cliente.close()



