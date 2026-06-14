frase = input("digite uma frase:").lower()
print(f"sua frase tem {frase.count("a")} letras a")
print(f"a letra a aparece na primeira na posição {frase.find("a")}")
print(f"a letra a a aparece na ultima vez na posiçâo {frase.rfind("a")}")