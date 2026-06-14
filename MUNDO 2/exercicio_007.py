a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("é um triangulo")
    triangulo = True
else:
    print("nao e um triangulo")
    triangulo = False


if triangulo == True:
    if a == b == c:
        print(" e equilatero")
    elif a == b or a == c or b == c or b == a or c == a or c == b:
        print("isoceles")
    elif a != b and a != c and b != a and b != c  and c != a and c != b:
        print("escaleno")