time = []
jogador = {}
gols = []
while True:
   jogador.clear()
   gols.clear()
   
   nome = jogador["nome"] = input("Nome:")
   partida = jogador["partidas"] = int(input(f"Quantas partidas {nome} jogou?: "))
   for j in range(1 ,partida + 1):
       gols.append(int(input(f"quantos gols {nome} fez na partida {j}:")))
   jogador["gols"] = gols[:]
   jogador["total"] = sum(gols)
   time.append(jogador.copy())
   while True:
       per = input("quer continuar[s/n}").strip().lower()[0]
       if per in "ns":
           break
       print("erro digite [s/n]")
   if per == "n":
       break
print("=-" * 20)
print(f'{"cod":<4} {"nome":<4} {"gols":<4} {"total":>20}')
print('_'* 40)
for pos, atleta in enumerate(time) :
    golstr = str(atleta['gols'])
    print(f"{pos:<4} {atleta['nome']:<4}  {golstr:<4} {atleta['total']:>15}")
print("_" * 40)
while True:
    dados = int(input("mostrar dados do jogador pelo seu codigo. [999 para parar]"))
    if dados == 999:
        break
    if dados >= len(time):
        print(f"nao existe jogador com esse codigo")
    else:
        print(f"levantamento do jogador: {time[dados]['nome']}")
        for i, golsp in enumerate(time[dados]["gols"]):
            print(f"na partida {i + 1} ele fez {golsp} gols")
print("VOLTE SEMPRE")
