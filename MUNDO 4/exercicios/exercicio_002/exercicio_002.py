class Gafanhoto:
    """
    essa classe cria um gafanhoto que tem nome e idade
    para criar uma nova pessoa use
    variavel = Gafanhoto(nome,idade)
    """

    def __init__(self,n,i):
        self.nome = ""
        self.idade = 0
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} Anos"

g1 = Gafanhoto("mauro",18)
print(Gafanhoto.__doc__)

