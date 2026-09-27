from rich import print
from time import sleep
class Livro:
    def __init__(self,nome,paginas):
        self.pagina = paginas
        self.nome = nome
        self.atual = 0
        self.resta = 0
        print(
            f"[blue]Você acabou de abrir o livro[/] [red]'{self.nome}'[/] [blue]que tem[/] [green]{self.pagina}[/] [blue]no total[/]. [blue]Você está na[/] [yellow]página {self.atual}[/] ")
    def avancar_pagina(self,qtde):
        pagina_anterior = self.atual
        self.atual += qtde
        self.resta = self.pagina - self.atual
        if self.resta <= 0:
            print("Voce terminou o Livro")
        else:
            for n in range(pagina_anterior + 1 ,self.atual + 1):
                print(f"Pág{n} > ",end="")
                sleep(0.5)
            print(f"vc andou {qtde} Paginas e esta na pagina {self.atual}")


l = Livro(nome="Era Das Trevas",paginas=30)

l.avancar_pagina(5)
l.avancar_pagina(4)
l.avancar_pagina(20)


