from utilidadesCeV.dados import dados
while True:
        inteiro = dados.leiavalor("Digite um numero inteiro: ")
        real = dados.leiafloat("digite um numero real: ")
        print(f"o numero inteiro é: {inteiro}")
        print(f"o numero real é: {real}")
        esc = input("continuar?").strip().lower()[0]
        while True:
            if esc in "sn":
              break
            else:
                print("digite s ou n")
        if esc == "n":
            break
