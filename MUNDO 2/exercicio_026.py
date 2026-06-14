a1 = int(input("digite o primeiro termo"))
r = int(input("digite a razão:"))
n =  10
termo_atual = a1
contador = 1
total = 0
mais = 10
while mais != 0:
    total +=  mais
    while contador <= total:
        print(f"{termo_atual}", end="")
        termo_atual += r
        contador += 1
    mais = int(input('quantos termos?'))
print("fim")