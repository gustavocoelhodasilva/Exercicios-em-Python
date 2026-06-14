from time import sleep
texto = {
    'limpa':    '\033[m',
    'preto':    '\033[30m',
    'vermelho': '\033[31m',
    'verde':    '\033[32m',
    'amarelo':  '\033[33m',
    'azul':     '\033[34m',
    'roxo':     '\033[35m',
    'ciano':    '\033[36m',
    'cinza':    '\033[37m',
    'branco':   '\033[97m'
}
fundo = {
    'preto':    '\033[40m',
    'vermelho': '\033[41m',
    'verde':    '\033[42m',
    'amarelo':  '\033[43m',
    'azul':     '\033[44m',
    'roxo':     '\033[45m',
    'ciano':    '\033[46m',
    'cinza':    '\033[47m',
    'branco':   '\033[107m'}
def titulo(msg,cor=0):
    tam = len(msg) + 4
    print(fundo['amarelo'])
    print("~" * tam)
    print(f"  {msg}  ")
    print("~" * tam )
    print(texto['limpa'])
def menu(txt):
    sleep(2)
    print("analisando..")
    sleep(1)
    help(mensagem)

    sleep(2)
while True:
    titulo("SISTEMA DE AJUDA PYHELP", )
    mensagem = input("Função ou Biblioteca>> ").strip()
    if mensagem == "fim":
        print('volte sempre')
        break
    else:
        menu(mensagem)

