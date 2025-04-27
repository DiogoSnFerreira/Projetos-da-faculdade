nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"Média: {media:.2f}")

if media > 6:
    print("Conceito: Aprovado")
elif 4 <= media <= 6:
    print("Conceito: Exame")
else:
    print("Conceito: Reprovado")
