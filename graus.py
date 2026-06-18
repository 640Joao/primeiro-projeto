graus = float(input("Graus da cidade: "))

if graus < 15:
    print("Frio")

elif graus >= 15 and graus <= 25:
    print("Clima agradavel")

else:
    print("Clima quente")
