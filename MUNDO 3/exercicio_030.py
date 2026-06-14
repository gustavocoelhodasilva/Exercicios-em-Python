def fatorial(n,show=True):
    """
    :param n: é o número que vai ser fatorado
    :param show: opcional para mostrar a conta
    :return: não retorna nada
    """
    conta = []
    f = 1
    for c in range(n,0, -1):
        f *= c
        conta.append(str(c))
    print(f)
    if show:
        print(f"{"x".join(conta)} = {f}")

fatorial(5,show=False)
help(fatorial)
