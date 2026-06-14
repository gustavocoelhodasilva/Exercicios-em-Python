# armazenamento de dados
pessoas = {}
lista = []
mulher = []
acima = []
som = 0
c = 0
while True:
    #leitura de dados
    pessoas.clear()
    pessoas['nome'] = input("nome: ")
    idade = pessoas['idade'] = int(input("idade"))
    som += idade
    while True:
        sexo = pessoas['sexo'] = input("sexo:").strip().lower()[0]
        if pessoas['sexo'] in "mf":
           break
        else:
            print("sexo invalido")
    if sexo == "f":
        mulher.append(sexo)
    lista.append(pessoas.copy())
    c += 1
    while True:
        esc = input("quer continuar[s/n]").strip().lower()[0]
        if esc in "sn":
            break
        print("erro responda [s ou n]")
    if esc == "n":
        break
media = som / c
for pessoa in lista:
        if pessoa['idade'] > media:
            acima.append(pessoa['nome'])
print('=-'*30)
# analise dos dados
print(f"foram cadastradas {c} pessoas")
print(f"a media de idade é {media:.1f}")
if len(mulher) != 0:
    print(f"{len(mulher)} mulheres foram cadastradas")
else:
    print("nenhuma mulher foi registrada")
if len(acima) != 0:
    for p in acima:
        print(f"pessoas com a idade maior que a media: {p}", end=" ")
else:
    print("nenhuma pessoa tem a idade maior que a media")
