from time import sleep

class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        print(f"{self.nome} é gafanhoto e tem {self.idade} Anos")

g1 = Gafanhoto()
pessoas = []

qtde_pessoas = int(input("Digite a Quantidade de pessoas que deseja cadrastar"))

for pessoa in range(qtde_pessoas):
    pessoa = Gafanhoto()
    pessoa.nome = input("Digite o nome").strip()
    pessoa.idade = int(input("Digite a Idade"))
    lista_de_pessoas = {"Nome":pessoa.nome,
             "Idade":pessoa.idade}
    pessoas.append(lista_de_pessoas)
print(pessoas)


