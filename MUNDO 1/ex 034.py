sl = float(input("digite seu salario:"))
if sl > 1250:
    au = sl * 0.10
    print(f"voce teve um aumento de 10% seu salario agora é {sl + au} reais")
else:
    au = sl * 0.15
    print(f"voce teve um aumento de 15% seu salario agora e de {sl + au}")