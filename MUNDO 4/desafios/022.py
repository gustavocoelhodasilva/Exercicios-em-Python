from rich import print
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.console import Group

class ControleRemoto:
    def __init__(self, volume=1, canal=1, maxcanal=5):
        self.ligar = False
        self.volume = volume
        self.canal = canal
        self.maximo = maxcanal

    def Ligar(self):
        self.ligar = not self.ligar
        self.mostrar_tela()

    def controle_volume(self, cmd=""):
        if self.ligar:
            if cmd == "+" and self.volume < 5:
                self.volume += 1
            elif cmd == "-" and self.volume > 0:
                self.volume -= 1
            self.mostrar_tela()
        else:
            print("[yellow]A TV está desligada![/yellow]")

    def Mudar_canal(self, cmd=""):
        if self.ligar:
            if cmd == ">":
                self.canal += 1
                if self.canal > self.maximo:
                    self.canal = 1
            elif cmd == "<":
                self.canal -= 1
                if self.canal < 1:
                    self.canal = self.maximo
            self.mostrar_tela()
        else:
            print("[yellow]A TV está desligada![/yellow]")

    def mostrar_tela(self):
        if self.ligar:
            # Destaca o canal atual
            canais_texto = ""
            for ch in range(1, self.maximo + 1):
                if ch == self.canal:
                    canais_texto += f"[bold black on yellow] {ch} [/] "
                else:
                    canais_texto += f" {ch}  "

            # Cria a barra de volume usando o Progress
            progress = Progress(
                TextColumn("[bold blue]VOLUME:[/]"),
                BarColumn(bar_width=15, complete_style="green", finished_style="green"),
                TextColumn("[bold green]{task.completed}/{task.total}[/]"),
            )
            progress.add_task("vol", total=5, completed=self.volume)

            # Agrupa os elementos gráficos (Texto dos canais + Barra de progresso)
            conteudo = Group(
                f"Canais: {canais_texto}\n",
                progress
            )

            visor = Panel(conteudo, title="[ TV ]", title_align="center", width=45)
            print(visor)
        else:
            visor = Panel("[red]Você Desligou a TV 🛑[/red]", title="[ TV ]", title_align="center", width=45)
            print(visor)


c = ControleRemoto()

while True:
    comando = input("Comandos (@ Power | < CH > | + VOL - | 0 Sair): ").strip()
    if comando == "@":
        c.Ligar()
    elif comando == "+":
        c.controle_volume("+")
    elif comando == "-":
        c.controle_volume("-")
    elif comando == ">":
        c.Mudar_canal(">")
    elif comando == "<":
        c.Mudar_canal("<")
    elif comando == "0":
        break