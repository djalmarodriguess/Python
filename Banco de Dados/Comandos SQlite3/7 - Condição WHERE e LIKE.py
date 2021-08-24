import sqlite3

cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes (nome text, sobrenome text, email text)" )


'''Condição WHERE
   Usado para fazer uma consulta no banco de dados a partir de uma informação especifica'''
#cursor.execute("SELECT * FROM clientes WHERE idade > 30 ")                  #EXEMPLO
#cursor.execute("SELECT * FROM clientes WHERE email = 'neymar@neyday.com'")  #EXEMPLO
#cursor.execute("SELECT * FROM clientes WHERE sobrenome = 'Rodrigues'")

'''Condição LIKE'''
#Usado para fazer uma consulta no banco de dados a partir de uma entrada não terminada
#cursor.execute("SELECT * FROM clientes WHERE email LIKE '%day.com'")         #EXEMPLO
cursor.execute("SELECT * FROM clientes WHERE email LIKE 'jo%'")              #EXEMPLO
registros = cursor.fetchall()


for clientes in registros :
    print(clientes)


cliente.commit()
cliente.close()



