def leiaint(mensagem):
    while True:
        try:
            txt = input(mensagem)
            num = int(txt)
        except ValueError, TypeError:
            print("\033[1;31mErro digite um numero valido\033[0m")
        except KeyboardInterrupt:
            print("\033[0;31mo usuario preferiou não informar dados\033[0m")
            break
        else:
            return num

