'''Programa de Registro e Login ao banco de dados.
Sem intereção com o usuário. '''


import sqlite3


def inserir():
    with sqlite3.connect('registro.db') as db:
        cursor = db.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS registro(nome TEXT, senha INTEGER )")

    print('Registre um novo usuário')
    usuario = input('Nome: ')
    senha = input('Senha: ')
    cursor.execute("SELECT 1 FROM registro WHERE nome = ? ", (usuario,))

    while len(cursor.fetchall()) > 0:
        print('Esse nome já existe. Tente novamente.')
        usuario = input('Nome: ')
        senha = input('Senha: ')
        cursor.execute("SELECT 1 FROM registro WHERE nome = ?", (usuario,))

    cursor.execute("INSERT INTO registro (nome, senha) VALUES (?,?)", (usuario,senha))
    
    print('Registrado')

    db.commit()

    cursor.execute("SELECT * FROM registro")
    registro = cursor.fetchall()
    for i in registro:
        print(i)

    db.close

def login():
    with sqlite3.connect('registro.db') as db:
        cursor = db.cursor()

    print('Logar em usuario existente')
    tentativas = 1
    usuario = input('Nome: ')
    senha = input('Senha: ')
    cursor.execute("SELECT 1 FROM registro WHERE nome = ? AND senha = ? ", (usuario, senha))
    
    if len(cursor.fetchall()) == 1:
        print('Logado')
        return

    while len(cursor.fetchall()) == 0 and tentativas < 3:
        print('Senha ou usuario errados')
        usuario = input('Nome: ')
        senha = input('Senha: ')
        cursor.execute("SELECT 1 FROM registro WHERE nome = ? AND senha = ?", (usuario, senha))
        tentativas += 1

        if len(cursor.fetchall()) == 1:
            print('Logado')
            return
        
        if tentativas >=3 :
            print('Número de tentativas excedeu 3 vezes')

    db.close()

#inserir()
login()
        
