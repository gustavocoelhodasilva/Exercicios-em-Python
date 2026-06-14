valor = float(input("digite o valor pago:"))
pag = int(input("digite 1 se vai pagar a vista/dinheiro, 2, a vista no cartao, 3, 2x vezes no cartao 4, 3x ou mais"))
if pag == 1:
    des = valor * 0.1
    print(f"ganhou 10% de desconto o preço agr é {valor - des} ")
elif pag == 2:
    des = valor * 0.05
    print(f"ganhou 5% de desconto o preço agr é {valor - des} ")
elif pag == 3:
    print(f"o preço é de {valor}" )
elif pag == 4:
    jur = valor * 0.2
    print(f"o produto com 20% de juros o preço agr é {valor + jur} ")
else:
    print("numero invalido")