a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("é um triangulo")
else:
    print("nao e um triangulo")

