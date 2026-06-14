def metade(num,formato=False):
    """
    -> serve para pegar um valor mostrar a metade o
    dobro e aumentado em quantos % vc definir
    e diminido tbm.
    :param num: Recebe o número que digitou.
    :param formato: Serve para se vc quiser a formatação R$ no número.
    :return: Retorna os valores de cada um das funções que chamar.
    """
    tot = num/2
    if formato == True:
        return moeda(tot)
    else:
        return tot


def dobro(num=0,formato=False):
    tot = num * 2
    if formato == True:
        return moeda(tot)
    else:
        return tot

def aumentar(num=0, porc=0, formato=False ):
    p  = (num * porc) / 100
    tot = num + p
    if formato == True:
        return moeda(tot)
    else:
        return tot
def reduzir(num, porc=0, formato=False ):
    p = (num*porc)/100
    tot  = num - p
    if formato == True:
        return moeda(tot)
    else:
         return tot

def moeda(txt):
    form = f"R${txt:.2f}"
    return form
def resumo(num=0,aum=10,dim=13):
    print(f"RESUMO".center(30,"="))
    print(f"valor analisado:\t {moeda(num)}")
    print(f"o dobro do preço\t {dobro(num,True)}")
    print(f"aumentado em {aum}%:\t {aumentar(num,aum,True)}")
    print(f"reduzido em {dim}%:\t {reduzir(num,dim,True)}")
    print("="*30)