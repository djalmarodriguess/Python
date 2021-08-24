import sqlite3

cliente = sqlite3.connect('cliente.db')
cursor = cliente.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS clientes (nome text, sobrenome text, email text)" )


'''Dados  serem inseridos de uma vez só.
   Criar uma lista e colocar dentro da mesma Tuplas com os dados que deseja inserir.'''
varios_registros = [('Roberta', 'Pereira', 'roberta@gmail.com'),
                    ('Ricardo', 'Araújo', 'ricardo@gmail.com'),
                    ('Neymar', 'Junior', 'neymar@neyday.com'),
                ]

'''Inserindo varios registro de uma vez no banco.
   Os sinais de "?" são de acordo com os números de dados que solicitou ao criar a tabela,
   nesse exemplo sao respectivamentes nome, sobrenome e email.
   *OBSERVAÇÃO IMPORTANTE = o comando agora é o nome do cursor".EXECUTEMANY"'''
cursor.executemany("INSERT INTO clientes VALUES (?,?,?)", varios_registros)

print('Clientes registrado com sucesso')

cliente.commit()
cliente.close()



