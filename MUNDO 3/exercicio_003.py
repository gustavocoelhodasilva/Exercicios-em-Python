valores = ( int(input(f"digite o 1º valor:")),int(input(f"digite o 2º valor:")),int(input(f"digite o 3º valor:")),int(input(f"digite o 4º valor:")))
print(f"voce digitou os valores {valores}", end="")
if 9 in  valores:
    print(f"\no valor 9 apareceu {valores.count(9)} vezes")
else:
    print("\no valor nove não apareceu")
if 3 in valores:
    print(f"o valor 3 apareceu pela primeira vez na posição {valores.index(3) + 1}")
else:
    print("o valor 3 n existe")

for i in valores:
    if i % 2 == 0:
        print(f"o valor {i} é par")