valor = int(input("digite o valor que quer sacar:"))
total = valor
ced  = 50
tot = 0
while True:
    if total >= ced:
        total -= ced
        tot += 1
    else:
        if tot > 0:
           print(f"total de {tot} cedulas de {ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
             ced = 1
        tot = 0
        if ced == 0:
            break
print("Volte sempre")
