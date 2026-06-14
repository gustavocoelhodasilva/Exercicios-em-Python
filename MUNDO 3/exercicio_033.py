def notas(*valores,sit=True):
    lista = list(valores)
    info = dict()
    info["total"] = len(lista)
    info["maior"] = max(lista)
    info["menor"] = min(lista)
    info["media"] = sum(lista)/ len(lista)
    if sit:
        if info["media"] <= 5:
            info["situação"] = "Ruim"
        elif info["media"] <= 7:
            info["situação"] = "Razoavel"
        elif info["media"] <= 10:
            info["situação"] = "Boa"
    print(info)
    return info

notas(1.3,4,5)