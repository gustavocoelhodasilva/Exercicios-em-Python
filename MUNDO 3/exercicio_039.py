from utilidadesCeV.moeda import moeda
from utilidadesCeV.dados import dados
p = dados.leiavalor("digite um valor: ")
moeda.resumo(p,10,30)
