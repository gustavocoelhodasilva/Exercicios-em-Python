from rich import print
class Funcionario:
    def __init__(self,nome,setor,cargo,empresa="Curso em video"):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa
    def Apresentar(self):
        return f"Olá me chamo [blue]{self.nome}[/blue] sou {self.cargo} e trabalho no setor de {self.setor} da empresa {self.empresa}"
c1 = Funcionario("Pedro","TI","Sênior")
print(c1.Apresentar())