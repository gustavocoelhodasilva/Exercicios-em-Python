import random
maior = menor = cont = 0
for n in range(1, 6):
    num = (random.randint(0, 5))
    cont += 1

    if cont == 1:
        maior = num
        menor = num
    else:
        if num < menor:
            menor = num
        if num >  maior:
            maior = num
    print(num, end=" ")
print(f"\no maior numero é {maior} e o menor {menor}")

