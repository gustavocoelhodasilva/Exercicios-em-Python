import os
import shutil

# Caminho da pasta onde estão os arquivos .py
pasta = r"/home/lenovo/Documentos/Exercicios-em-Python/MUNDO 4/"

for arquivo in os.listdir(pasta):
    caminho = os.path.join(pasta, arquivo)
    if os.path.isfile(caminho) and arquivo.endswith(".py"):
        # Nome da pasta = nome do arquivo sem extensão
        nome_pasta = os.path.splitext(arquivo)[0]
        pasta_destino = os.path.join(pasta, nome_pasta)

        # Cria a pasta se não existir
        os.makedirs(pasta_destino, exist_ok=True)

        # Move o arquivo para dentro da pasta
        shutil.move(caminho, os.path.join(pasta_destino, arquivo))
        print(f"Movido: {arquivo} ➜ {nome_pasta}/")