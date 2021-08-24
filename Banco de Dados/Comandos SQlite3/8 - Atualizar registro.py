import sqlite3

cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()

'''Atualizar registro.
   Escreva o local da tabela de onde deseja modificar, já escreva em seguida o item que será adicionado.
   Em "WHERE", entrar com "rowid" e informar em qual linha se encontra o item a ser modificado'''

''' 1º Maneira:'''
#cursor.execute("UPDATE clientes SET nome = 'Carla' WHERE sobrenome = 'Nunes' ")  #EXEMPLO

'''2º Maneira: Aqui foi feito a modificação de um cliente por inteiro, por isso 3 "cursor".'''
cursor.execute("UPDATE clientes SET nome = 'Leonel' WHERE rowid = 5")
cursor.execute("UPDATE clientes SET sobrenome = 'Messi' WHERE rowid = 5")
cursor.execute("UPDATE clientes SET email = 'messi@et.com' WHERE rowid = 5")

'''O comando "rowid," tem que está abilitato para o cursor conseguir identificar aonde 
   fazer a mudança.'''
cursor.execute("SELECT rowid,* FROM clientes")
registros = cursor.fetchall()


for clientes in registros :
    print(clientes)


cliente.commit()
cliente.close()



