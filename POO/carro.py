class Carro:
    def __init__(self, nome, modelo, cor, ano, valor, andando = False, parado = False, telefone = False ):
        self.nome = nome
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.andando = andando
        self.parado = parado
        self.telefone = telefone


    def andar(self):
        if self.andando:
            print(f'{self.nome} já esta andando de carro')
            return

        if self.telefone:
            print(f'{self.nome} precisa desligar o telefone antes de ligar o carro')
            return
            
        print(f'{self.nome} está andando de {self.modelo} {self.cor}.')
        self.andando = True


    def parar(self):
        if not self.andando:
            print(f'{self.nome} já esta parado')
            return 
                 
        print(f'{self.nome} parou de andar de {self.modelo}')
        self.andando = False

    def ligar_telefone(self):
        if self.andando:
            print(f'{self.nome} não pode falar no telefone enquanto dirige.')
            return

        print(f'{self.nome} está parado e no telefone')
        self.telefone = True

    def desligar_telefone(self):
        if not self.telefone:
            print(f'O telefone ja está desligado')
            return
        print(f'Desligando telefone')
        self.telefone = False