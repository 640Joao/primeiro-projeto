numero = 0
for i in range(1,101):
    if i % 2 != 0 and  i % 3 == 0:
        numero += i
        print(numero)