aluno = dict()
aluno["nome"] = input("Nome: ")
aluno["media"] = int(input(f"media de {aluno["nome"]}"))
if aluno["media"] >= 6:
    print("A situção é igual a aprovado")
elif aluno["media"] >=  4:
    print(" a situação é igual a recuperação")
else:
    print("a situação é igual a reprovado")
