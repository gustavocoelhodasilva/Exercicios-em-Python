a = float(input("digite um primeiro numero"))
b = float(input("digite o segundo numero"))
c = float(input("digite o terceiro numero"))
maior = b
menor = a
if (b < a) and (b < c):
    menor = b
if (c < b) and (c < a):
    menor = c
print(f"o menor numero foi {menor}")
if (b > a) and (b > c):
    maior = b
if (a > b) and (a > c):
    maior = a
if (a < c) and (c > b):
    maior = c
print(f"o maior numero foi o {maior}")