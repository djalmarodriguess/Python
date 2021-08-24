from random import randint

class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def gerar_id():
        sortear_id = randint(100,999)
        return sortear_id


p1 = Pessoa('Djalma', 25)
print(f'O id sorteado é: {p1.gerar_id()}')


