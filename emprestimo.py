salario = float(input("Qual é o seu salário bruto: "))
parcelas = float(input("Digite o valor das parcelas: "))

porcentagem = salario * 0.30
print(porcentagem)

if parcelas > porcentagem:
    print("O emprestimo não foi aprovado")

else:
    print("O emprestimo foi aprovado")