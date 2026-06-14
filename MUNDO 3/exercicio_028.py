import random
from time import sleep

def sortear():
    for n in range(0,6):
        num = random.randint(0,20)
        numeros.append(num)
    print(f"sorteando {len(numeros)} valores: ", end="")
    for v in numeros:
        print(f" {v} ", end="")
        sleep(0.3)
def somarpar(numeros):
    for v in numeros:
        if v % 2 == 0:
            valores[0].append(v)
        else:
            valores[1].append(v)
    if len(valores[0]) > 0:
        print(f"\nvalores pares {valores[0]}")
        print(f"a soma de todos valores pares são {sum(valores[0])}")
    else:
        print(f"so existem valores impares: {valores[1]}")

numeros = []
sortear()
valores = [[], []]
somarpar(numeros)