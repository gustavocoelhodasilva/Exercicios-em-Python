def mostrar():
    print("=-" * 20)
    print("de 1 a 10 de 1 em um:")
    print("=-" * 20)
    for n in range(1, 11):
        print(f"{n}", end=" ")
    print("fim")
    print("=-" * 20)
    print("de 10 a 0 de 2 em 2:")
    print("=-" * 20)
    for n in range(10, -1, -2):
        print(f"{n}", end=" ")
    print("fim")
    print("=-" * 20)

def contador(inicio, fim, passo):
    print(f"contagem de {inicio} ate o {fim} de {passo} em {passo}")
    print("=-" * 20)
    if passo < 0:
        passo = -1
    if passo == 0:
        passo = 1
    
    if inicio > fim:
        for i in range(inicio,fim -1 ,passo):
            print(f"{i}",end=" ")
        print("fim")
    else:
        for i in range(inicio,fim +1 ,passo):
            print(f"{i}", end=" ")
        print("fim")
mostrar()
print("agora é sua vez de personalizar a contagem: ")
contador(inicio=int(input("inicio: ")), fim=int(input("Fim:")), passo=int(input("passo: ")))