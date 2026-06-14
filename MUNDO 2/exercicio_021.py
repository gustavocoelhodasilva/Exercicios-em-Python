somaidade = 0
mediaidade = 0
maioridadehomem = 0
menoridadedemulher = 0
nomevelho = ""
for p in range(1,5):
    print(f"----------{p}º PESSOA----------- ")
    nome = input("nome: ").strip()
    idade = int(input("idade:"))
    sexo = input("Sexo[M/F]: ").strip().upper()
    somaidade += idade
    if p == 1 and sexo in "M":
        maioridadehomem = idade
        nomevelho = nome
    if maioridadehomem < idade and sexo == "M":
        maioridadehomem = idade
        nomevelho = nome
    if sexo == "F" and idade < 20:
        menoridadedemulher += 1


mediaidade = somaidade / 4
print(f"A media da idade dos integrantes é : {mediaidade}")
print(F"o mais velho tem {maioridadehomem} e se chama {nomevelho}")
print(F"há {menoridadedemulher} mulheres de menos de 20 anos")