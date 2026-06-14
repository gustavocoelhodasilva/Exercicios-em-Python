import random
vit = 0
par = 0
impar = 0
while True:
    user = int(input("diga um valor:"))
    computador = random.randint(0,11)
    total = user + computador

    if total % 2 == 0:
        par = total
    else:
        impar = total
    escolha = ' '
    while escolha not in "PpIi":
          escolha = input("par ou impar[p/i]").strip().lower()
    print(f"voce jogou {user} e o computador {computador} = {total}")
    if escolha in "Pp" and par == total:
        print(f"Você ganhou {par} é par")
        vit += 1
    elif escolha in "Ii" and impar == total:
        print(f"Você ganhou {impar} é impar")
        vit += 1
    else:
        print(f"PERDEU OTARIO")
        break
print(f"Você ganhou {vit} vezes")