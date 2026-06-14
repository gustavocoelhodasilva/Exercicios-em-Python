mostra_pares =  []
par = 0
for i in range(0,6):
    n = int(input("Digite um numero inteiro:"))
    if n % 2 == 0:
        par += n
        mostra_pares.append(n)
print(f"numeros pares: {mostra_pares}")
print(f"a soma dos numeros pares é {par}")
