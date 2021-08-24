from dados import mostrar_dados, pesquisar, pesquisar_id


num = input('Qual numero de telefone com o DDD: ')
print()
ddd_num = num[0:2]
n = int(ddd_num)

if n == 11:
    pesquisar(n)
    print()
if n == 14:
    pesquisar(n)
    print()
if n == 15:
    pesquisar(n)
    print()
if n == 21:
    pesquisar(n)
    print()
if n == 22:
    pesquisar(n)
    print()
if n == 24:
    pesquisar(n)
    print()
if n == 37:
    pesquisar(n)
    print()
lista =  [11, 14, 15,21, 22, 24, 37]
if n not in lista:
    print('DDD NÃO ENCONTRADO')
    print()
    mostrar_dados()
    print()
    escolha = int(input('Qual das cidades acima, digite apenas o ID? '))
    print()
    pesquisar_id(escolha)



