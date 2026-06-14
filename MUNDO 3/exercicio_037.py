from utilidadesCeV.moeda import moeda
n = float(input("digite um preço: "))
print(f"a metade de {moeda.moeda(n)} é {moeda.metade(n, True)}")
print(f"o dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}")
print(f"aumentando 10% de {moeda.moeda(n)} é {moeda.aumentar(n, 10, True)}")
print(f"o reduzindo 13% de  {moeda.moeda(n)} é {moeda.reduzir(n, 13, True)}")