import sqlite3

cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()

'''Limite de resultado
#Simplesmente para limitar a amostragem dos dados'''
cursor.execute("SELECT rowid,* FROM clientes LIMIT  2 ")  #Mostra apenas os dois primeiros clientes
cursor.execute("SELECT rowid,* FROM clientes ORDER BY rowid DESC LIMIT  2 ")  #Mostra apenas os dois ultimos clientes
registros = cursor.fetchall()


for clientes in registros :
    print(clientes)


cliente.commit()
cliente.close()



