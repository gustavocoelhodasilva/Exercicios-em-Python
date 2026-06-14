# Exercício 004
listagem = (
    "Notebook Gamer", 4599.90,
    "Mouse Sem Fio", 89.90,
    "Teclado Mecânico", 250.00,
    "Monitor 24' IPS", 899.00,
    "Headset Bluetooth", 199.90,
    "Cadeira Ergonômica", 1200.00,
    "Webcam Full HD", 349.00,
    "SSD 1TB NVMe", 420.50,
    "Memória RAM 16GB", 299.90,
    "Suporte articulado", 150.00
)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f"{listagem[pos]:>5}")