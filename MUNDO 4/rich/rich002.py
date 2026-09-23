from rich import print
from rich.panel import Panel

caixa = Panel("[bold white]Está é uma mensagem[/]", title="Mensagem", style="blue",width=20)
print(caixa)