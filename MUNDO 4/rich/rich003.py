from rich import print
from rich.table import Table

tabela = Table(title="Tabela",style="blue",width=50)

tabela.add_column("Jogo",justify="center")
tabela.add_column("Preço",justify="center")
tabela.add_row("God of war" ,"65R$")

print(tabela)