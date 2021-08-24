import sqlite3

cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()


'''Ordenando em ordem crescente de acordo com a linha'''
cursor.execute("SELECT rowid,* FROM clientes ORDER BY rowid")

'''Ordenando em ordem decrescente de acordo com a linha'''
cursor.execute("SELECT rowid,* FROM clientes ORDER BY rowid DESC")

'''Ordenando pelo sobrenome - Ordem alfabetica'''
cursor.execute("SELECT rowid,* FROM clientes ORDER BY sobrenome ")

'''Ordenando pelo nome - Ordem alfabetica'''
cursor.execute("SELECT rowid,* FROM clientes ORDER BY nome ")
registros = cursor.fetchall()


for clientes in registros :
    print(clientes)


cliente.commit()

cliente.close()



