import sqlite3

cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()

'''Apagar a tabela por inteira do registro.
   *OBS: Esse comando não foi exetutado, para aproveitamento da tabela nos exemlos a frente.'''
cursor.execute("DROP TABLE clientes ")


cursor.execute("SELECT rowid,* FROM clientes ")
registros = cursor.fetchall()


for clientes in registros :
    print(clientes)


cliente.commit()
cliente.close()



