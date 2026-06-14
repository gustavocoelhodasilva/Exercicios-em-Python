from datetime import date
ano = int(input("digite seu ano de nascimento"))
atual  = date.today().year
idade = atual - ano
print(f"voce nasceu em {ano} e tem aproximadamente {idade} anos")
if idade < 18:
    print("nao pode se alistar no exercito")
    print(f"falta {18 - idade} anos")
elif idade == 18:
    print("e hora de se alistar")
else:
    print("ja passou da hora de se alistar")
    print(f"ja se passaram {idade - 18} anos")


