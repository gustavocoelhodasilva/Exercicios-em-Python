valores = []
for v in range(0, 6):
    num = int(input(f"digite o {v}º valor: "))
    if v == 0 or num > valores[-1]:
        valores.append(num)
        print("adicionado ao final da lista")
    else:
        pos = 0
        while pos < len(valores):
            if pos <= valores[pos]:
                valores.insert(pos, num)
                print(f"na posiçaõ {pos} foi adicionado o valor {num}")
                break
print(f"os valores ordenados são {valores}")