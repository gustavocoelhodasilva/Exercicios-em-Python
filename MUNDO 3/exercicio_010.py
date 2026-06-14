# Exercício 010
numeros = []
pares = []
impares = []
while True:
    n = int(input("digite um numero:"))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    per = input("quer parar[s/n]:").strip().lower()[0]
    if per == "s":
        break
print(f"valores digitados: {numeros}")
print(f"numeros pares {pares}")
print(f"numeros impares {impares}")
