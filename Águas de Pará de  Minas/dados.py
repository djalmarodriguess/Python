import sqlite3 

con = sqlite3.connect('agua.db')
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS agua(id INTEGER PRIMARY KEY, cidade TEXT, ddd INTEGER)")

ADICIONAR_DADOS = "INSERT INTO agua(cidade, ddd) VALUES(?,?)"

ADICIONAR_VARIOS = "INSERT INTO agua(cidade, ddd) VALUES(?,?)"

MOSTRA_DADOS = "SELECT * FROM agua "

PESQUISAR_PELO_DDD = "SELECT * FROM agua WHERE ddd = (?)"

PESQUISAR_PELO_ID = "SELECT * FROM agua WHERE id = (?)"


def adicionar(cidade, ddd):
    cursor.execute(ADICIONAR_DADOS, (cidade,ddd))
    
def adicionar_varios(lista):
    cursor.executemany(ADICIONAR_VARIOS, (lista))

def pesquisar(ddd):
    cursor.execute(PESQUISAR_PELO_DDD, (ddd,))
    registro = cursor.fetchall()
    cont = 0
    for i in registro:
        cont += len(str(i[0])) 
        print(f'|{cont+0}| {i[1]:^18}| {i[2]:>0}|')
    print()
    if cont == 1:
        print()
        pergunta = str(input(f'Você é da cidade de {i[1]}?[S/N]:  ')).upper()
        print()
        if pergunta == "N":
            mostrar_dados()
            print()
            escolha = int(input('Qual das cidades acima, digite apenas o ID? '))
            print()
            pesquisar_id(escolha)
    else:
        pergunta = str(input(f'Você é de algumas dessa cidades?[S/N]: ')).upper()
        print()
        if pergunta == "S":
            escolha = int(input('Qual das duas? ')) 
        else:
            mostrar_dados()
            escolha = int(input('Qual das cidades acima, digite apenas o ID? '))
            print()
            pesquisar_id(escolha)
   
def pesquisar_id(id):
    cursor.execute(PESQUISAR_PELO_ID, (id,))
    registro = cursor.fetchall()
    for i in registro:
         print(f'|{i[0]}| {i[1]:^18}| {i[2]:>0}|')


def mostrar_dados():
    cursor.execute(MOSTRA_DADOS)
    registro = cursor.fetchall()
    print('----     ---------     ----- ')
    print(' ID       CIDADES       DDD')
    print('----     ---------     ----- ')
    for i in registro:
        print(f'|{i[0]:<2}| {i[1]:^18}| {i[2]:>0}|')
        con.commit()
        

lista = [('Votorantim', 15 ),
('Agulhas Negras', 24 ),
('Jaú', 14 ),
('Juturnaíba', 22 ),
('Pará de Minas', 37 ),
('Niterói', 21 ),
('Condessa', 11 ), ]

#adicionar_varios(lista)
#mostrar_dados()

