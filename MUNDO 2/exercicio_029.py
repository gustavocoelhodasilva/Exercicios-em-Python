num = cont = som = 0
num = int(input("digite algum numero [999 para parar]"))
while num != 999:
    som += num
    cont += 1
    num = int(input("digite algum numero [999 para parar]"))
print(f"vc digitou {cont} valores com a soma {som}")