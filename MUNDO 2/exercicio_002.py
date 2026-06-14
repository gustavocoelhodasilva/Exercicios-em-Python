

print("Escolha uma das opções:")
print('''{1} para base binaria/  
{2} para base octal/  
{3} para base hexadecimal/''')
per = int(input(">>>"))
if per == 1:
    bim = int(input("digite um numero para converter em binario"))
    print(bin(bim))
elif per == 2:
    oc = int(input("digite um numero para converter em octal"))
    print(oct(oc))
elif per == 3:
    he = int(input("digite um numero para converter em hexadecimal"))
    print(hex(he))
