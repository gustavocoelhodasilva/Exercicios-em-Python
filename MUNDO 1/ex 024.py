cdd = input("digite o nome da sua cidade").lower().strip()
cmc = cdd.split()
if cmc[0] in "santo":
    print("sua cidade começa com santo")
else:
    print("sua cidade nao comeca com santo")
