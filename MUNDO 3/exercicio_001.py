tabela_brasileirao = (
    "Palmeiras", "Flamengo", "Fluminense", "Athletico-PR", "Red Bull Bragantino",
    "Coritiba", "São Paulo", "Bahia", "Cruzeiro", "Botafogo",
    "Vitória", "Atlético-MG", "Internacional", "Grêmio", "Corinthians",
    "Vasco da Gama", "Santos", "Mirassol", "Clube do Remo", "Chapecoense"
)
print(f"lista de times{ tabela_brasileirao}")
print(f"os cinco primeiros times {tabela_brasileirao[0:5]}")
print(f"os quatro ultimos {tabela_brasileirao[-4:]}")
print(f"times em ordem alfabetica {sorted(tabela_brasileirao)}")
print(f"a posição do chapecoense é {tabela_brasileirao.index("Chapecoense") - 1} lugar")