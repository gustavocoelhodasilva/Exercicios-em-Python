import math
oposto = float(input("digite o cateto oposto"))
adjacente = float(input("digite o cateto adjacente"))
hipotenusa = math.hypot(oposto, adjacente)
print(f"a hipotenusa é {hipotenusa}")
