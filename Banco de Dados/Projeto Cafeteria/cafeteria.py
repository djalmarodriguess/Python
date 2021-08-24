import sqlite3


'''Criar banco de dados'''
cafe = sqlite3.connect('cafe.db')
cursor = cafe.cursor()

'''Criar tabelas com suas respectivas colunas'''
CRIAR_BD = "CREATE TABLE IF NOT EXISTS cafe (id INTEGER PRIMARY KEY, nome TEXT, metodo TEXT, avaliação INTEGER)"


'''Foi feito de forma separada toda estrutura dos comandos do SQlite3 a serem adicionados no cursor.execute.'''
ADICIONAR_UM  = "INSERT INTO cafe (nome, metodo, avaliação) VALUES(?,?,?)"

MOSTRAR_TABELA = "SELECT * FROM cafe"

PESQUISAR_NOME = "SELECT * FROM cafe WHERE nome = (?)"

MELHOR_CAFÉ = " SELECT * FROM cafe ORDER BY avaliação DESC LIMIT 1"

DELETAR_TUDO = "DROP TABLE cafe"

DELETAR_UM = "DELETE FROM cafe WHERE id = (?)"


def adicionar_um(nome, metodo, avaliação):
    cursor.execute(ADICIONAR_UM, (nome,metodo,avaliação))


def melhor_cafe():
    cursor.execute(MELHOR_CAFÉ)
    registro = cursor.fetchall()

    for i in registro:
        print(f'{i[0]} - {i[1]}, {i[2]} ,{(i[3])}')


def deletar_um(id):
    cursor.execute(DELETAR_UM, (id,))
    

def deletar_tudo():
    cursor.execute(DELETAR_TUDO)
    registro = cursor.fetchall()

    for i in registro:
        print(i)
       

def criar_bd():
    cursor.execute(CRIAR_BD)
    

def pesquisar_nome(nome):
    cursor.execute(PESQUISAR_NOME, (nome,))
    registro = cursor.fetchall()

    for i in registro:
        print(f'{i[0]} - {i[1]}, {i[2]} ,{(i[3])}')


def mostrar_tabela ():
    cursor.execute(MOSTRAR_TABELA)
    registro = cursor.fetchall()

    for i in registro:
        print(f'{i[0]} - {i[1]}, {i[2]} ,{(i[3])}')


    cafe.commit()

criar_bd()