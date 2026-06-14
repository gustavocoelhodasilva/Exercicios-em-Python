per = media = cont = maior = menor = som = 0
while per != "n":
    n = int(input("digite um valor inteiro:"))
    per = input("quer continuar [s/n]").lower().strip()
    som = n + n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
media = som/cont
print(f"voce digitou {cont} numeros e a media foi de {media}")
print(f"o maior numero foi {maior} e o menor foi o {menor}")

