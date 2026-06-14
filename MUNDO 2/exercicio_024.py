import time
v1 = float(input("digite um valor:"))
v2 = float(input("digite outro valor"))
maior = 0
while True:
    time.sleep(1)
    print("-"*20)
    print('''
    SOMAR[1]
    MULTIPLICAR[2] 
    MAIOR[3]
    NOVOS NUMEROS[4]
    SAIR DO PROGRAMA[5]''')
    print("-"*20)
    op = int(input("Digite a opção >>>>"))
    if op == 1:
        time.sleep(1)
        print(f"{v1} + {v2} = {v1 + v2}")
    elif op == 2:
        time.sleep(1)
        print(f"{v1} x {v2} = {v1 * v2}")
    elif op == 3:
        if v1 > v2:
           maior += v1
           time.sleep(1)
           print(f"o maior numero foi o {maior}")
        elif v1 < v2:
            maior += v2
            time.sleep(1)
            print(f" o maior numero foi o {maior}")
    elif op == 4:
        v1 = float(input("digite um valor:"))
        v2 = float(input("digite outro valor"))
    elif op == 5:
        print("saindo...")
        time.sleep(3)
        break


