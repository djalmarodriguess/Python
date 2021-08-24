class BancoDeDados:
    def __init__(self, x, y, z):
        self.publico = x
        self._protegido = y
        self.__privado = z


encapsulamento = BancoDeDados(
    'Arquivo publico', 
    'É publico mas não deve ser acessado', 
    'Não pode ser acessado de fora da classe'
)

print(encapsulamento.publico)
print(encapsulamento._protegido)
print(encapsulamento._BancoDeDados__privado)


