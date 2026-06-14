c = 0
s = 0
for n in range(0,501):
    if n % 3 == 0 and n % 2 != 0:
        s = s + n
        c = c + 1
print(f" a soma dos numeros é {s}")
print(f" no intervalo tem {c} numeros")

