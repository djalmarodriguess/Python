import json
'''jogador = {
    "nome": "Bruno",
    "time": "Galo doido",
    "vivo": True,
    "energia": 100,
    "mochila": ["pederneira", "corda", "linha", "arame"],
    "aeronave": [
        {"tipo": "transporte", "habilidade": 80},
        {"tipo": "ataque", "habilidade": 100},
        {"tipo": "reconhecimento", "habilidade": 50}
    ]
}'''

jogador_j = '{"nome": "Bruno","time": "Galo doido","vivo": "True","energia": 100,"mochila": ["pederneira", "corda", "linha", "arame"],"aeronave": [{"tipo": "transporte", "habilidade": 80},{"tipo": "ataque", "habilidade": 100},{"tipo": "reconhecimento", "habilidade": 50}]}'

jogador = json.loads(jogador_j)
'''for k in jogador.keys():
    print(k)'''

'''for a in jogador['aeronave']:
    print(a['tipo'] + ' - ' + str(a['habilidade']))'''

print(f'O jogador de nome {jogador["nome"]}, com energia de {jogador["energia"]}HP,tem uma {jogador["mochila"][1]} na mochila.')

for a in jogador['aeronave']:
    if a["tipo"] in "ataque":
        print(f'tem uma aeronave de {a["tipo"]} e {a["habilidade"]} de habilidade')


nome = str(input("Nome: ")).strip()
print(len(nome))
print(nome.title())
print(nome.capitalize())
print(nome.upper())
print(nome.lower())