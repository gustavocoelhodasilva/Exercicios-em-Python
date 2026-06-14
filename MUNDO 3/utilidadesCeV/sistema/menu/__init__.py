from exercicio_032 import leiaint
from time import sleep
def linha(tam=42):
    return "=" * tam

def cabecalho(txt):
    sleep(0.6)
    layout = f"{linha()}\n\033[0;35m{txt.center(42)}\033[0m\n{linha()}"
    return layout


def lista(lst):
    sleep(0.6)
    print(cabecalho("\033[0;36mMENU PRINCIPAL\033[0m"))
    c = 1
    for i in lst:
        print(f"\033[0;33m{c}\033[0m{'-'*15}\033[0;34m{i}\033[0m")
        c += 1
 
    op = leiaint("\033[1;35mSua opção:\033[0m ")
    return op

