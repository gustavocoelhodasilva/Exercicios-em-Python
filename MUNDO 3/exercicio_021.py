jogador = dict()
partida = list()
jogador["nome"] = input("Nome: ")
tot = int(input(f"quantas partidas {jogador['nome']} jogou: "))
for c in range(1, tot+1):
    partida.append(int(input(f"quantos gols fez na partida {c}")))
jogador["gols"] = partida[:]
jogador["total"] = sum(partida)

for k, v in jogador.items():
    print(f"no campo {k} há {v}")
print(f"o jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")

for i,v in enumerate(jogador['gols']):
    print(f"=> na partida {i + 1} fez {v} gols")