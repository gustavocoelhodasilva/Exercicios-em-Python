import random
aluno1 = input("digite o nome do primeiro aluno")
aluno2 = input("digite o nome do segundo aluno")
aluno3 = input("digite o nome do terceiro aluno")
aluno4 = input("digite o nome do quarto aluno")
alunos = [aluno1, aluno2, aluno3, aluno4]
ordem = random.shuffle(alunos)
print(f"a ordem de apresentação é:")
print(alunos)