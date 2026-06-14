valores = []
for v in range(1, 6):
    valores.append(int(input(f"Digite o {v}º valor:")))
for i in valores:
    print(f"{i}", end=" ")
print(f"\no maior valor é {(max(valores))} e esta na posição {valores.index(max(valores))}")
print(f"\no menor valor é {min(valores)} e esta na posição {valores.index(min(valores))}  ")

