from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []
    def Add_favoritos(self,jogo):
        self.jogos.append(jogo)
        self.jogos.sort()
    def ficha(self):
        lista_jogos_formatada = "\n".join([f":video_game: [blue]{jogo}[/]"for jogo in self.jogos])
        ficha = Panel(f"Nome Real: [bold black on blue]{self.nome}[/]\nJogos favoritos: \n{lista_jogos_formatada} ", title=f"Jogador <{self.nick}>", title_align="center",width=40)
        print(ficha)

g = Gamer("Benicio","bene")
g.Add_favoritos("God of War")
g.Add_favoritos("Sonic")
g.ficha()