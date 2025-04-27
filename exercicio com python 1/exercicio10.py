media = float(input("Digite a média final do aluno: "))

if media > 6 and media < 7:
    print("Você precisa estudar mais!")
elif media >= 7 and media <= 9:
    print("Muito bem! Continue fazendo mais exercícios.")
elif media > 9:
    print("Parabéns! Excelente desempenho!")
else:
    print("Nota inválida ou muito baixa.")