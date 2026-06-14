from math import pow
peso = float(input("digite seu peso"))
altura = float(input("digite sua altura"))
imc = peso/ (pow(altura, 2))
print(f"seu imc é {imc:.1f}")
if imc < 18.5:
    print("abaixo do peso")
elif imc < 25:
    print("normal")
elif imc  < 30:
    print("sobrepeso")
elif imc < 40:
    print("obesidade grau I")
else:
    print("obesidade grau II")