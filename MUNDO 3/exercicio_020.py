from datetime import datetime
dados = dict()
dados["nome"] = input("Nome: ")
nasc = int(input("ano de nascimento: "))
ano = datetime.now().year
idade = ano - nasc
dados["idade"] = idade
dados["ctps"] = int(input("carteira de trabalho: [0 nao tem]"))
if dados["ctps"] != 0:
    dados["contratação"] = int(input("ano de contratação: "))
    dados["salario"] = float(input("salario: "))
    dados["aposentadoria"] = dados["idade"] + (dados["contratação"] + 35) - ano
for k, v in dados.items():
    print(f"-{k}: {v}")
