from rich import print
class Caneta:
    def __init__(self,cor):
        self.cor = cor
        self.tampa = True
        self.quebra = False
    def destampar(self):
        self.tampa = False
    def quebrar(self,qtde):
        self.quebra = True
        if self.quebra:
            for q in range(qtde):
                print()



    def escrever(self,frase):
        if self.tampa == False:
            cor = self.cor
            if cor == "verde":
                print(f"[green]{frase}[/]")
            elif cor == "vermelha":
                print(f"[red]{frase}[/]")
            elif cor == "azul":
                print(f"[blue]{frase}[/]")
        else:
            print(f":no_entry_sign: Destampe a Caneta antes de escrever")


c1 = Caneta("verde")
c2 = Caneta("azul")
c3 = Caneta("vermelha")
c1.destampar()
c1.escrever("oi")
c2.escrever("oi")
c3.escrever("oi")
