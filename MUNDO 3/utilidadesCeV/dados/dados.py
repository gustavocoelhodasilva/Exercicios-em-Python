def leiavalor(msg):
    valido = False
    while valido == False:
        try:
            entrada = str(input(msg)).replace(",",".").strip()
            if entrada == "":
                return 0
            else:
                num = int(entrada)
        except (ValueError, TypeError):
            print(f"erro digite apenas numeros validos")
        except KeyboardInterrupt:
            print("o usuario decidiu n informar os numeros")
            break
        except Exception as erro:
            print(f"deu erro de tipo {erro.__class__} causa de {erro.__cause__}")
        else:
            valido = True
            return num
def leiafloat(msg):
    valido = False
    while valido == False:
        try:
            entrada = str(input(msg)).replace(",",".")
            if entrada == "":
                return 0
            else:
              num = float(entrada)
        except (ValueError,TypeError):
            print(f"foi encontrado erro no tipo do dado digite apenas numeros reais")
        except KeyboardInterrupt:
            print("o usuario não quis informar dados")
            return 0
        except Exception as erro:
            print(f"foi encontrado um erro de classe{erro.__class__} de causa {erro.__cause__}")
        else:
            valido = True
            return num