a1 = int(input("digite o primeiro termo"))
r = int(input("digite a razão:"))
n =  10
termo = a1
c = 0
while n > c:
    print(f"{termo} --> ", end="")
    termo += r
    c += 1

print("fim")