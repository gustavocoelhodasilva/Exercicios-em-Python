import time
import random
jogos = []
dado = []
per = int(input("quantos jogos quer q eu gere:"))
for e in range(per):
    for j in range(6):
        num = random.randint(0,60)
        dado.append(num)
        if len(dado) == 6:
            jogos.append(dado[:])
            dado.clear()
for l in jogos:
    print(f"jogo {jogos.index(l) + 1}: {l}")
    time.sleep(1)
    