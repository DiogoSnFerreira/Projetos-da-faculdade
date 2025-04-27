# Começa com o total zerado
total_recebido = 0
total_gasto = 0

# Vai repetir 12 vezes (uma vez pra cada mês do ano)
mes = 1
while mes <= 12:
    recebido = float(input("Digite o valor RECEBIDO no mês {}: ".format(mes)))
    gasto = float(input("Digite o valor GASTO no mês {}: ".format(mes)))

    total_recebido = total_recebido + recebido
    total_gasto = total_gasto + gasto

    mes = mes + 1  # Vai pro próximo mês

# Mostra os totais no final do ano
print("Total recebido no ano: R$", total_recebido)
print("Total gasto no ano: R$", total_gasto)

# Calcula a diferença
diferenca = total_recebido - total_gasto

# Verifica se houve lucro ou prejuízo
if diferenca > 0:
    print("Houve LUCRO de R$", diferenca)
elif diferenca < 0:
    print("Houve PREJUÍZO de R$", -diferenca)
else:
    print("Não houve lucro nem prejuízo.")