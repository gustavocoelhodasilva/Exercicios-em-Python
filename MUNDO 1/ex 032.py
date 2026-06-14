from datetime import date
ano = int(input("digite um ano ou coloque 0 para o ano atual:"))
if ano == 0:
    ano = date.today().year
    print(ano)
if ano % 4 == 0 and ano % 100 != 0  or ano % 400 == 0:
    print("e ano bissexto")
else:
    print("nao e bissexto")