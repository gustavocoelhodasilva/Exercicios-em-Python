from utilidadesCeV.sistema import menu
from exercicio_032 import leiaint

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criar_arquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print("ouve um erro na criação do arquivo")
    else:
        print(f"arquivo {nome} criado com sucesso")
def ler(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Deu erro na leitura do arquivo")
        return False
    else:
        print("Aquivo aberto com sucesso")
        print(menu.cabecalho("Pessoas cadastradas"))
        print(a.read())
        return True
def cadastrar(nome,idade):
    n = input(nome)
    i = leiaint(idade)
    pessoas = dict()
    pessoas[n] = i
    with open('Pessoas.txt', 'a', encoding="utf-8") as arquivo:
        for k,v in pessoas.items():
            arquivo.write(f"{k.capitalize()}: {v}\n")
        arquivo.write("\n")
def apagar(arq):
    try:
        a =  open(arq, "w")
    except:
        print("Erro ao apagar conteudo do arquivo")
    else:
        print("conteudo apagado com sucesso")