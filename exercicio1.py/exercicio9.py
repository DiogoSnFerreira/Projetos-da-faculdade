salario_minimo = float(input("Digite o valor do salário mínimo: "))
salario = float(input("Digite o seu salário atual: "))


if salario < 2 * salario_minimo:
    # reajuste de 45%
    novo_salario = salario + (salario * 0.45)
elif salario < 5 * salario_minimo:
    # reajuste de 35%
    novo_salario = salario + (salario * 0.35)
else:
    # reajuste de 25%
    novo_salario = salario + (salario * 0.25)

print("Seu novo salário é: R$", novo_salario)