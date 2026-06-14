total =0
mais =0
contador = 0
menor = 0
nomebarato = " "
while True:
    nome = input("digite o nome do produto:")
    preco = float(input("digite o preço do produto:"))
    contador += 1
    total += preco
    if preco > 1000:
        mais += 1
    if contador == 1:
        menor = preco
        nomebarato = nome
    else:
        if preco < menor:
            menor = preco
            nomebarato = nome
    op = input("quer continuar [s/n]").strip().lower()
    if op == "n":
        break
print(f"o total gasto foi {total}R$")
print(f"{mais} produtos passaram de 1000R$")
print(f"o produto mais barato foi o {nomebarato} custando {menor}R$")
