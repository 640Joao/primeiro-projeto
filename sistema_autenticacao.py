usuario = input("Digite o nome de usuário: ")
token = int(input("Digite a chave de segurança (token inteiro): "))


if usuario == "admin" and token == 9988:
    print("Acesso concedido. Bem-vindo!")
else:
    print("Dados de acesso inválidos")