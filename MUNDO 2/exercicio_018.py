palavra = input("digite uma frase").strip()
invertida = ""
for letra in palavra:
    invertida =  letra + invertida
if invertida == palavra:
    print(F"e um palindromo pois {palavra} de tras pra frente é {invertida}")
else:
    print(F"nao e pois forma isso {invertida}")