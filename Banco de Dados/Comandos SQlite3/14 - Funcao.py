import sqlite3

'''Será visto todos os comandos anteriores mas com funções para agilizar o processo. '''


cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()


'''Adicionar um novo registro'''
def adicionar_um(nome, sobrenome, email):
    cursor.execute("INSERT INTO clientes VALUES(?,?,?)", (nome, sobrenome, email))

'''Deletetar um registro a partir da linha.'''
def deletar(id):
    cursor.execute("DELETE FROM clientes WHERE rowid = (?)", (id,))

'''Adicionar varios registros de uma vez apenas.
   Colocar em uma lista todos os dados dos clientes.'''
def adicionar_varios(lista):
    cursor.executemany("INSERT INTO clientes VALUES(?,?,?)", lista)

'''Pequisar um registro pelo email
Necessario fazer o "for" para mostrar apenas o valor desejado'''
def procurar_email(email):
    cursor.execute("SELECT rowid, * FROM clientes WHERE email = (?)", (email,))
    registros = cursor.fetchall()

    for clientes in registros :
        print(clientes)


'''Consultar Banco de dados e mostrar todos os registros.'''
def mostrar_todos():
    cursor.execute("SELECT rowid,* FROM clientes ")
    registros = cursor.fetchall()

    for clientes in registros :
        print(clientes)

    cliente.commit()

'''Função adicionar apenas um registro'''
#adicionar_um('Marta', 'Assis', 'marta@assis.com')


'''Função deletar, informar o número da linha para fazer a exclusão'''
#deletar(6)


'''Função adicionar vários registros 
   Fazer uma lista com os dados dos clientes e chamar na função a lista.'''
registros = [
    ('Maria', 'Joaquina', 'maria@hotmail.com'),
    ('Benzama', 'Françua', 'benzama@hotmail.com'),
    ('Firmino', 'Liverpool', 'firmino@paraiba.com'),
]
#adicionar_varios(registros)

'''Função de pesquisa através de um email'''
#procurar_email('roberta@gmail.com')


'''Função mostrar dados'''
mostrar_todos()




