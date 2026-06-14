while True:
    num  = int(input("digite um numero:[digite negativos para parar]"))
    if num < 0:
        break
    for n in range(0,11):
        print(f"{num} X {n} = {num*n}")