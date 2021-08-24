import sqlite3

'''Será feito um tutorial passso a passo de como utilizar um banco de dados em "sqlite3", 
um tutorial que será pedido aos "clintes" apenas 3 informações, nome, sobrenome e email'''

'''Criar, conectra o bando de dados e o cursor
   Será com o cursor que faremos as manipulações no banco de dados'''
cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()

'''Criar tabela = Create table
   É como se fosse criar as estruturas de uma tabela em excel, dando os nomes de linhas e colunas.'''

#cursor.execute("CREATE TABLE clientes (nome text, sobrenome text, email text)" )

'''Para não ficar criando uma nova tabela toda vez que rodar o programa, usamos:'''
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (nome text, sobrenome text, email text)" )

'''Tipos de dados = Data type
#text
#integer
#real
#null
#blob'''

'''Praticar nosso comando.
   Tudo que esta entre esse comando e "connect" será executado'''
cliente.commit()
'''Fechar conecção'''
cliente.close()



