import random
jogadores = {}
for j in range(0,5):
    nome = input(f"Nome do jogador {j}")
    dado = random.randint(1,6)
    jogadores[nome] = dado
for nome,dado in jogadores.items():
    print(f"o jogador {nome} tirou {dado}")
    print("=+"* 30)
print("GANHADOR: ")
ranking = sorted(jogadores.items(), key= lambda item: item[1], reverse=True)

for pos, (nome, dado) in enumerate(ranking, start=1):
    print(f"o jogador {nome} tirou {dado} e é o {pos} lugar")