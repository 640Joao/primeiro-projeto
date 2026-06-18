nascimento = int(input("Digite o ano de seu nascimento: "))

idade = 2026 - nascimento

print(idade)

if idade >=16:
    print("Acesso ao filme liberado!")

else:
    print("Acesso bloqueado: Conteúdo não recomendado para menores de 16 anos.")

