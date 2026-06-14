alunos = []
dado = []
media = 0
while True:
    dado.append(input("digite o nome do aluno: "))
    dado.append(float(input("digite a primeira nota do aluno: ")))
    dado.append( float(input("digite a segunda nota do aluno: ")))
    alunos.append(dado[:])
    dado.clear()
    per = input("quer continuar[s/n]").strip().lower()[0]
    if per == "n":

        break
print(f"alunos cadastrados: {alunos}")

for l in alunos:
    soma =  l[1] + l[2]
    media = soma / 2
    print("No. Nome   Media")
    print(f"{alunos.index(l) + 1}   {l[0]}    {media}")

while True:
        esc = int(input("mostrar notas de qual aluno? ex: 1. [999 para sair]"))
        if esc == 999:
            break
        po = esc - 1
        aluno_selecionado = alunos[po]
        print(f" as notas de {aluno_selecionado[0]} a primeira nota:{aluno_selecionado[1]}/ segunda nota: {aluno_selecionado[2]}")
print("finalizando..")
print("volte sempre")