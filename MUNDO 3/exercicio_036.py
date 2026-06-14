from utilidadesCeV.moeda import moeda

p = float(input("digite o preço R$: "))
print(f"metade de  {p} é: {moeda.metade(p)}")
print(f"o dobro de {p} é:  {moeda.dobro(p)}")
print(f"com aumento de 10%: {moeda.aumentar(p)}")
print(f"reduzindo 13%: {moeda.reduzir(p)}")