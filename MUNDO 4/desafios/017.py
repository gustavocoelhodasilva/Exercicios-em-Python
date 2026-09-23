from rich import print
from rich.table import Table

class Produto:
    def __init__(self,nome="produto não cadastrado",preco="preco não cadastrado"):
        self.nome = nome
        self.preco = preco
    def etiqueta(self):
        etiqueta = Table(title="Produto",show_header=False )
        etiqueta.add_row(f"{self.nome}")
        etiqueta.add_row(f"{self.preco}R$")
        print(etiqueta)
p = Produto("notebook",30000)
p.etiqueta()