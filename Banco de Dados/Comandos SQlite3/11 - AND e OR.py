import sqlite3

cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()

'''Comando - AND
   É necessario atender todas as solicitações do usuario
   Nesse exemplo foi solicitado o cliente de sobrenome que começa com "Ro" e que esteja na linha 2.'''
cursor.execute("SELECT rowid,* FROM clientes WHERE sobrenome LIKE 'Ro%' AND rowid = 2 ")


'''Comando - OR
   É necessario atender uma ou outra solicitação do usuario
   Nesse exemplo foi solicitado o cliente de sobrenome que termina 
   com "drigues" ou que esteja na linha 2.
   Como a primeira solicitação ("%drigues") foi atendida, mostra-se todos os clientes com essa informação.'''
cursor.execute("SELECT rowid,* FROM clientes WHERE sobrenome LIKE '%drigues' OR rowid = 2 ")
registros = cursor.fetchall()


for clientes in registros :
    print(clientes)


cliente.commit()
cliente.close()



