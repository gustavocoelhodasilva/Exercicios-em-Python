import random
from time import sleep
class Banco:
    def __init__(self, total= 0, titular=""):
        self.titular = titular
        self.id = random.randint(0,1000)
        self.total = 0
        print(f"Bem vindo {self.titular}. Conta criado com sucesso seu id é {self.id}")
        print(f"Seu saldo atual é de {self.total}")
        sleep(2)
    def __str__(self):
        return f"Seu saldo atual é {self.total}"
    def __getstate__(self):
        return f"Nome= {self.titular} \n ID: {self.id} \n Saldo:{self.total}"

    def depositar(self,qtde=0):
        if qtde >= 0:
            self.total += qtde

            print(f"Você depositou {qtde} reais")
        else:
            print("Depósito negado")

    def sacar(self,qtde = 0):
        if qtde >= 0:
           if qtde < self.total:
               self.total -= qtde
               print(f"Saque de {qtde} realizado com sucesso")
           else:
               print(f"Saque negado")
b = Banco(titular="gustavo")
while True:
    print("=" * 20)
    print("Bem Vindo ao Banco")
    print("="*20)
    print("[1]-Ver saldo")
    print("[2]-Depositar")
    print("[3]-Sacar")
    print("[4]-Ver Perfil")
    print("[5]-Sair")
    print("-" * 20)
    per = int(input(">>>"))
    if per == 1:
         print(b)
         sleep(2)
    elif per == 2:
        deposito = float(input("Quanto deseja depositar? "))
        b.depositar(deposito)
        sleep(2)

    elif per == 3:
        saque = float(input("Quanto deseja sacar? "))
        b.sacar(saque)

        sleep(2)
    elif per == 4:
        print(b.__getstate__())


    elif per == 5:
        print("tenha um ótimo dia")
        break
    else:
        print("Digite uma resposta válida")