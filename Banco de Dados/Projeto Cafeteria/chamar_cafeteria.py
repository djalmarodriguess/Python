'''Um simples projeto para aplicar as ferramentas aprendidas no SQlite3

O objetivo é gerar a integação do usuário com as opções disponiveis

As funções estao no arquivo (cafeteria.py)'''

import cafeteria

'''Descrição das opções para interação do usuário'''
cardapio  = ''' 
          -- Cafeteria --
Por favor escolha uma dessas opções:

1) Adicionar novo sabor de café.
2) Ver todos os sabores disponíveis.
3) Encontre um café pelo nome.
4) Veja qual café tem a melhor avaliação.
5) Retirar um sabor do cardápio.
6) Limpar toda tabela
7) Sair.
 '''

'''Fiz um laço de repetição while True para que o programa tenha fim somente quando o usuário desejar, ou seja, apertando a opção 7'''
while True:    
    print(cardapio)
    escolha  = int(input('Sua escolha: '))

    '''Para a opção 1 o usuário deve cadastra o nome do café, o método e uma avaliação'''    
    if escolha == 1:
        nome = str(input('Entre com o nome do café: ')).strip().capitalize()
        metodo = str(input('Entre com o método de fabricação: ')).strip().capitalize()
        avaliacao = int(input('Entrar com a avaliação: '))
        cafeteria.adicionar_um(nome, metodo, avaliacao)
        cafeteria.mostrar_tabela()

    elif escolha == 2:
        cafeteria.mostrar_tabela()
        
    elif escolha == 3:
        nome = str(input('Entre como nome que deseja fazer a pesquisa: ')).capitalize().strip()
        cafeteria.pesquisar_nome(nome)

        '''Para a opção 4, será feito uma pesquisa em todo o banco de dados, mostrando somente aquela item com maior nota na avaliação'''
    elif escolha == 4:
        cafeteria.melhor_cafe() 

        '''Para a exclusão de um item é necessário apenas informar o ID, todas as opções serão mostradas na tela antes da escolha e após a mesma.'''
    elif escolha == 5:
        cafeteria.mostrar_tabela()
        deletar  = int(input('Entre com o número do id para fazer a exclusão do item: '))
        cafeteria.deletar_um(deletar)
        print()
        print('NOVA TABELA')
        cafeteria.mostrar_tabela()


        '''Opção 6 faz a exclusão por inteira do banco de dados, por isso foi colocado uma pergunta de confirmação, pois pode haver um engano da parte do usuário, e será aceito somente as letras "S/N" para execução. '''
    elif escolha == 6:
        cafeteria.mostrar_tabela()
        deletar_tudo = str(input('Tem certeza que deja limpar o banco de dados?[S/N]: ')).upper()[0]
        while deletar_tudo not in "SN":
            deletar_tudo = str(input('OPÇÃO INVÁLIDA, SOMENTE [S/N]: ')).upper()[0]
            if deletar_tudo  == 'S':
                cafeteria.deletar_tudo()
                print('NÃO HÁ DADOS')
            else:
                pass

        '''Caso o usuário digite valores que não sejam de 1 a 7, aparecerá a mensagem de erro.'''
    elif escolha > 7 or escolha < 1 :
        print('NÃO TEMOS ESSA OPÇÃO TENTE NOVAMENTE')
        
        '''Por fim, se o usuário digitar 7 será finalizado o programa, e para confirmação da escolha se é feita uma pergunta antes, aceitando apenas "S/N" como resposta.'''
    elif escolha == 7:
        certeza = str(input('Tem certeza que deja sair?[S/N]: ')).upper()[0]
        while certeza not in "SN":
            certeza = str(input('OPÇÃO INVÁLIDA, SOMENTE [S/N]: ')).upper()[0]
        if certeza  == 'S':
            break
        else:
            pass
print('FIM PROGRAMA, OBRIGADO')




