idade = int(input("digite a idade do atleta:"))
print(f"idade do atleta: {idade}")
if idade <= 9:
    print("mirim")
elif idade <= 14:
    print("infantil")
elif idade <= 19:
    print("junior")
elif idade <= 20:
    print("senior")
elif idade > 20:
    print("master")