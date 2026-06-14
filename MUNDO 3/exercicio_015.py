matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = scol = mai = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"digite um numero para {l},{c}"))
for l in range(0,3):
    for c in range(0,3):
       print(f"[{matriz[l][c]}]", end="")
       if matriz[l][c] % 2 == 0:
           spar += matriz[l][c]
    print()
for l in range(0,3):
    scol += matriz[l][2]
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif c < mai:
        mai = matriz[1][c]

print(f"a soma dos numeros pares é {spar}")
print(f"a soma da terceira coluna é {scol}")
print(f"o maior numero no meio é {mai}")


