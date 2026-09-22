class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} Anos"

g1 = Gafanhoto()


