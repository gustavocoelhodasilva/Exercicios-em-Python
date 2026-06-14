valor = float(input("Digite o valor da casa:"))
salario = float(input("\033[4;32;32mDigite o seu salario do comprador:\033[m"))
ano = float(input("Quantos anos de financiamento?"))
prestacao = (valor/(ano * 12))
sl = salario * 0.3
total_meses = int(ano * 12)
print(f"para pagar uma casa de {valor:.2f}, serão {total_meses} prestações de {prestacao:.2f}R$")
if prestacao > sl:
    print(f"sua prestação de {prestacao:.2f} por mes nao pode financiar pela casa pois exede o limite de 30% do seu salario")
else:
    print(f"prestacão aprovada. Voce pagara {total_meses} parcelas de {prestacao:.2f} por mês")