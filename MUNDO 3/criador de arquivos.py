import os

# Cole o caminho da sua pasta dentro das aspas, mantendo o 'r' antes delas
caminho_da_sua_pasta = r"D:\CURSO EM VIDEO\PYTHON\MUNDO 3"

for i in range(45):
    numero_formatado = f"{i:03d}"
    nome_arquivo = f"exercicio_{numero_formatado}.py"

    caminho_completo = os.path.join(caminho_da_sua_pasta, nome_arquivo)

    with open(caminho_completo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"# Exercício {numero_formatado}\n")

print("Diz que foi agora, por favor!")