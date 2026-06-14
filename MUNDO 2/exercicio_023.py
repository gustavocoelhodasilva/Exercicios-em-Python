import random
ia = random.randint(1,11)
print("ADVINHE O NUMERO")
p = 1
while p != ia:
    p = int(input("qual numero eu pensei?"))
    print("EROUUUU")
    p += 1
    if p == ia:
        print(f"o numero que eu pensei foi {ia}")
        print(f"voce teve que jogar {p} vezes pra acerta seu burro")
        print("ACERTOU MISERAVI")