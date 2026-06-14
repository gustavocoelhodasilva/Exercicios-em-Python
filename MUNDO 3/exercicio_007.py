lista = []
while True:
    num = int(input("digite um numero:"))
    if num in lista:
        lista.remove(num)
        print(f"não pode numeros repetidos não sera adicionado no final")
    else:
        lista.append(num)
        lista.sort()
        print("valor adicionado com sucesso....")

    esc = input("que continuar[s/n]").strip().lower()[0]
    if esc == "n":
        break
print(f"numeros em ordem de tamanho: {lista}")
