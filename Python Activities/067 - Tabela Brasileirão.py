tabela = ("Flamengo", "Internacional", "Atlético Mineiro", "São Paulo", "Fluminense", "Grêmio",
          "Palmeiras", "Santos", "Athletico-PR", "Corinthians", "Bragantino", "Ceará", "Atlético-GO",
          "Sport", "Bahia", "Fortaleza", "Vasco da Gama", "Goiás", "Coritiba", "Botafogo")
print(f'Os 5 primeiros são: {tabela[0:5]}')
print('=='*50)
print(f'Os 4 ultimos são: {tabela[-4:]}')
print('=='*50)
print(f'A tabela em Ordem alfabética : {sorted(tabela)}')
print('=='*50)
bragantino = tabela.index("Bragantino")
print(f'A posição do Bragantinno é a {bragantino+1}º posição')