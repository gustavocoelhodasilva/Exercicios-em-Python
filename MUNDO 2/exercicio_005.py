n1 = float(input(" digite a primeira nota"))
n2 = float(input("digite a segunda nota"))
soma = n1 + n2
media = soma/2
if (media > 5) and (media < 6.9):
    print("de recuperação")
    print(f"com uma media de {media}")
elif media < 5:
    print("reprovado")
    print(f"com uma media de {media}")
elif media > 7:
    print("aprovado")
    print(f"com uma media de {media}")
