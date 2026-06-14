def ficha(n="<desconhecido>",g=0 ):
    print(f"o jogador {n} fez {g} gols")

nome = input("nome:")
gols = input("quantos gols: ")
if gols.isnumeric():
     gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome,gols)
