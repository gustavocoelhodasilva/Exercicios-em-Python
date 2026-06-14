maior = 0
menor = 0
for p in range(1,6):
  peso =  float(input(f"digite seu peso pessoa {p}: >>"))
  if p == 1:
      menor = p
      maior = p
  elif peso > maior:
      maior = peso
  elif peso < menor:
      menor = peso
print(f"o maior peso foi de {maior}kg")
print(f"o menor peso foi de {menor}kg")
