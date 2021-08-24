import sqlite3

cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()

'''Deletar Registro
   Apenas informar o "rowid" que todos os dados do usuario será apagado'''
cursor.execute("DELETE FROM clientes WHERE rowid = 5 ")


'''O comando "rowid," tem que está abilitato para o cursor conseguir identificar o que excluir.'''
cursor.execute("SELECT rowid,* FROM clientes")
registros = cursor.fetchall()


for clientes in registros :
    print(clientes)


cliente.commit()
cliente.close()



