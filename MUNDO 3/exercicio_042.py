from utilidadesCeV.sistema import menu
lst = []
while True:
    esc = input("\033[1;31mAdicione opções ao sistema: \033[0m")
    lst.append(esc)

    try:
        while True:
            per = input("\033[0;36mContinuar? \033[0m").strip().lower()[0]
            if per in "sn":
                break
            else:
                print("\033[0;31mdigite apenas s ou n\033[0m")
        if per == "n":
            break
    except (ValueError,TypeError):
        print("\033[0;31mdigite apenas sim ou não\033[0m")
lst.append("sair")
while True:
   try:
        resposta = menu.lista(lst)
        if resposta == len(lst):
            print("\033[0;36mSaindo.....\033[0m")
            break
        if 1 <= resposta < len(lst):
             print(menu.cabecalho(lst[resposta-1]))
        else:
            print("\033[0;31mNão encontrado.\033[0m \033[0;33mDigite uma opção válida\033[0m")
   except(TypeError, ValueError) as erro:
       print(f"\033[0;35mDesculpe tivemos um erro tecnico do tipo {erro.__class__} por causa de {erro.__cause__}\033[0m ")
       break
   except Exception as erro:
       print(f"tivemos um erro do tipo {erro.__class__} por causa de {erro.__cause__}")
