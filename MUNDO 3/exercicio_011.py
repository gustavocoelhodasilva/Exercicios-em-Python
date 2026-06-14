while True:
    num = input("digite uma expressão: ")
    pilha = []
    for c in num:
        if c  == "(":
            pilha.append(c)
        else:
            if c == ")":
                pilha.append(c)
    if len(pilha) == 0:
        print("digite alguma coisa")
    if len(pilha) % 2 ==0 and len(pilha) != 0 :
        print("isso e uma expressão valida")
        break
    else:
        if len(pilha) != 0:
            print("nao é uma expressão valida")
            break
