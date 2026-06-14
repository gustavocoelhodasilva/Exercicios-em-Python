from time import sleep
import random
lista = []
while True:
    qtde = int(input("digite a quantidade de valores inteiros que queira gerar:"))
    for v in range(qtde):
        val = random.randint(0,1000)
        lista.append(val)
    sleep(1)
    print("valores adicionados..")
    sleep(1)
    print(f"valores: {lista}")

    while True:
        resp = input("quer parar? [s/n]").strip().lower()[0]
        if resp in "sn":
            break
        else:
            print("erro digite novamente:")
    if resp == "s":
            break
def mostrar(lista):
    print("analisando valores.....")
    sleep(1)
    for i in lista:
        print(f" {i} ", end="")
        sleep(1)
    print(f"foram informados: {len(lista)} valores ao todo")
    sleep(1)
    print(f"o maior valor informado foi: {max(lista)}")
mostrar(lista)