a1 = int(input("digite o primeiro termo"))
r = int(input("digite a razão:"))
n  = int(input("digite a quantidade de termos:"))
termo_atual = a1
print("sequencia so PA:",  end=" ")

for i in range(n):
    print(termo_atual + r, end=" ")
    termo_atual += r
