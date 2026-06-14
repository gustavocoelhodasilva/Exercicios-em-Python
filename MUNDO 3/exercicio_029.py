from datetime import datetime
def voto(ano):
        if ano < 18:
           return "NEGADO"

        elif ano >= 18 and ano < 70:
            return "OBRIGATORIO"
        else:
              return "OPCIONAL"


nasc = int(input("digite seu ano de nascimento: "))
idade = datetime.now().year - nasc
voto = voto(idade)
print(f"voce tem {idade} anos e seu voto é {voto}")