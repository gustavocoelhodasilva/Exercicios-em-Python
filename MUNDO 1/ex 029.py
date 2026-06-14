vel = float(input("digite a velocidade que estava"))
m = 80
if vel > m:
    valor = vel - m
    print("voce recebeu uma multa de 7 reais por km acima da velocidade de 80km")
    print(f"voce esta com {valor * 7} para pagar")
else:
    print("parabens voce esta certo")

