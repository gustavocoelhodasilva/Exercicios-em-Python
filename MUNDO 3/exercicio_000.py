numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez", "onze",
    "doze", "treze", "quatorze", "quinze", "dezesseis",
    "dezessete", "dezoito", "dezenove", "vinte"
)
while True:
    num = int(input("Digite um numero:"))
    if 0 <= num <= 20:
        for i in numeros_extenso:
            if num == numeros_extenso.index(i):
                print(f"você digitou o numero {i}")
    else:
         print("tente novamente")

    esc = input("quer continuar[s/n]").strip().lower()[0]
    if esc == "n":
        break

