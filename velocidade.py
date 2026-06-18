import random

velocidade_carro = random.randint(0, 100)
print(f"Sua velocidade {velocidade_carro}")

if velocidade_carro > 80:
    print("Você foi multado!")

else:
    print("Boa viagem!")