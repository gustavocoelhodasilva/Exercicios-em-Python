from rich import print
from rich.panel import Panel
class Churrasco:
    def __init__(self,nome="churras",pessoas=1):
        self.nome = nome
        self.pessoas = pessoas
        self.consumo = 0.4
        self.preco = 82.40
    def analisar(self):
        total_carne = self.consumo* self.pessoas
        total_custo = self.preco * total_carne
        total_pagar = total_custo / self.pessoas




        caixa = Panel(f"Analizando [green]{self.nome}[/green] com [blue]{self.pessoas} Convidados[/] \n"
                      f"Cada pessoa consumira {self.consumo} de carne e cada kg custa {self.preco:.2f}Kg\n"
                      f"Recomendo [blue]{total_carne:.1f}kg[/] de carne\n"
                      f"O custo total será de [green]{total_custo:.2f}R$[/]\n"
                      f"Cada pessoa deverá pagar [green]{total_pagar:.2f}R$[/]", title=f"{self.nome}",width=100)
        print(caixa)

c = Churrasco("Churras brabo",100000)
c.analisar()