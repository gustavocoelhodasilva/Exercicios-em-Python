lista = []
while True:
    nome = int(input("digite um valor:"))
    lista.append(nome)
    esc = input("quer continuar[s/n]").strip().lower()[0]
    if esc == "n":
        break
print(f"quantos numeros digitados:  {len(lista)}")
lista.sort(reverse=True)
print(f"valores descrecente {lista}")

if 5 in lista:
    print("cinco esta na lista")
else:
    print("o cinco nao esta na lista")

