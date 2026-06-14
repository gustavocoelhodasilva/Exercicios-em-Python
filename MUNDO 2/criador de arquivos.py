import os

# Cole aqui o caminho completo da sua pasta existente
caminho_da_pasta = r"D:\PYTHON\CURSO EM VIDEO mundo 2"

# 1. APAGA OS ARQUIVOS ANTERIORES (do 006 ao 036) PARA LIMPAR A PASTA
for i in range(6, 37):
    nome_antigo = os.path.join(caminho_da_pasta, f"exercicio_{i:03d}.py")
    if os.path.exists(nome_antigo):
        os.remove(nome_antigo)

# 2. CRIA OS 36 ARQUIVOS NOVOS (do 001 ao 036)
for i in range(1, 37):
    nome_novo = os.path.join(caminho_da_pasta, f"exercicio_{i:03d}.py")
    with open(nome_novo, "w", encoding="utf-8") as f:
        pass

print("Concluído! Pasta limpa e arquivos do exercicio_001.py ao exercicio_036.py criados.")
