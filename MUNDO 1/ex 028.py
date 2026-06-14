import random
numero = random.randint(0,5)
player = int(input("adivinhe o numero de 0 a 5 que escolhi !"))
if player == numero:
    print(f"parabens vc acertou o numero era: {numero}")
elif player > 5:
    print("numero invalido")
else:
    print(f"voce errou o numero era {numero}")