palavras = ("aprender", "estudar", "python", "java")
for i in palavras:
    print(f"\nna palavra {i} temos:", end=" ")
    for l in i:
         if l in "aeiou":
           print(l, end=" ")