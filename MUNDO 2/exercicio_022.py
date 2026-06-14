while True:
    s = input("Digite seu sexo [M/F]:").upper()
    if s != "M" and s != "F":
        print("esse sexo n existe.")
    else:
      if s == "M":
        print("vc passou seu sexo é masculino")
        break
      elif s == "F":
          print("vc passou seu sexo é feminino")
          break
