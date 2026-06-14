dis = float(input("digite a distancia da viagem"))
if dis < 200:
    preco = dis * 0.5
    print(f"ate 200km são 0.5 centavos por km. vc ira pagar {preco} reais")
else:
    preco = dis * 0.45
    print(f"de 200km para cima vc paga 0.45 por km. vc ira pagar {preco} reais")