valores = [[],[]]
for v in range(0,7):
    num = ( int(input("digite um valor: ")))
    if num % 2 == 1:
        valores[0].append(num)
        valores[0].sort()
    else:
        valores[1].append(num)
        valores[1].sort()
print(f"impares: {valores[0]} pares: {valores[1]}")
