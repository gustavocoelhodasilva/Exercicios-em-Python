import random
from time import sleep
opcoes = ["pedra", "papel", "tesoura"]
ia = random.choice(opcoes)
per = input("pedra, papel, ou tesoura").strip().lower()
print("\033[1;31;31mJO\033[0m")
sleep(1)
print("\033[1;34;34mKEN\033[0m")
sleep(1)
print("\033[1;33;33mPÔ\033[0m")
sleep(1)

print(f"voce jogou: \033[1;31;37m{per}\033[0m")
sleep(1)
print(f'a ia jogou \033[1;34;37m{ia}\033[0m')

if per not in opcoes:
    print("opcao invalida")

if ia == "pedra" and per == "tesoura" or ia == "tesoura" and per == "papel" or ia == "papel" and per == "pedra":
    print("você \033[1;30;31mPerdeu\033[0m ")
elif ia == per:
    print("\033[1;35;35mEMPATE\033[0m")
else:
    print("voce \033[1;30;32mGanhou\033[0m")
