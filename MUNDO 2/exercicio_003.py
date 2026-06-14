a = int(input("digite um valor"))
b = int(input("digite outro valor"))
if a > b:
    print(f"o valor de {a} é maior")
elif b < a:
    print(f"o valor {b} e o maior")
elif a == b:
    print("ambos valores sao iguais")