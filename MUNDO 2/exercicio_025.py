num = int(input("digite um numero"))
fac = 1
numor = num
while num > 1:
    fac *= num
    num -= 1
    print(f"Multiplicando: {fac} x {num} =", end=" ")
    print(f"{fac}")
print(f"{numor} = {fac}")