pessoas = []
dados = []
while True:
     dados.append(input("digite seu nome: "))
     dados.append(float(input("digite seu peso")))
     pessoas.append(dados[:])
     dados.clear()
     per = input("quer continuar[s/n]").strip().lower()[0]
     if per == "n":
         break
maior = pessoas[0][1]
menor = pessoas[0][1]
pesados = []
leves = []

for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
      menor = p[1]
for p in pessoas:
    if p[1] == maior:
        pesados.append(p[0])
    if p[1] == menor:
        leves.append(p[0])

print(f"foram cadastradas {len(pessoas)} pessoas")
print(f"pessoas mais pesada {pesados} ")
print(f"pessoas mais leves {leves}")