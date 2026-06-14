#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
maior = homem = mulher = 0
while True:
    idade = int(input("digite sua idade: "))
    sexo = ' '
    while sexo not in "MF":
       sexo =  input("digite seu sexo[M/F]: ").upper().strip()
    opcao = input("quer continuar? [s/n]").lower().strip()
    if opcao == "n":
        break
#A) quantas pessoas tem mais de 18 anos.
    if idade > 18:
        maior += 1
#B) quantos homens foram cadastrados.
    if sexo == "M":
        homem += 1
#C) quantas mulheres tem menos de 20 anos.
    if sexo == "F":
        if idade < 20:
            mulher += 1
print(f"tem {maior} pessoas maiores de 18 anos")
print(f"{homem} homens foram cadastrados")
print(f"tem {mulher} mulheres menores que vinte anos")