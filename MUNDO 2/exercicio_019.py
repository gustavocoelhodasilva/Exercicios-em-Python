from datetime import datetime
maior = 0
menor = 0
for p in range(1,8):
    nasc = int(input(f"digite o seu ano de nascimento pessoa {p}:"))
    ano = datetime.now().year
    idade = ano - nasc
    if idade >= 18:
        print(f"é maior de idade tem {idade} anos")
        maior += 1
    elif idade < 18:
        print(f"é menor de idade tem {idade} anos")
        menor += 1
print(f"{maior} pessoas são maiores e {menor} pessoas sao menores")