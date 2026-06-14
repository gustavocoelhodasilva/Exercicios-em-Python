cont = som = 0
while True:
    n = int(input("Digite um numero inteiro: [999 para parar]"))

    if n == 999:
        break
    cont += 1
    som += n
print(f"a soma dos numeros foi igual a = {som}")
print(f"você digitou {cont} numeros.")