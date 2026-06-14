tot = 0
num = int(input("digite um numero inteiro:"))
for c in range(1, num + 1):
    if num % c == 0:
        print(f"\033[34m {c} \033[m", end="")
        tot += 1
    else:
        print(f"\033[31m {c} \033[m", end="")
print(f"\no numero {num} e divisivel {tot} vezes")
if tot != 2:
    print("ele nao e primo")
else:
    print("e primo")
