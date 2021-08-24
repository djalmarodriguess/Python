from datetime import datetime

class Pessoa:
    ano_atual = datetime.now().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def por_ano_de_nascimento(cls,nome,ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome,idade)


p1 = Pessoa.por_ano_de_nascimento('Djalma', 1995)
print(f'{p1.nome} tem {p1.idade} anos de idade')


