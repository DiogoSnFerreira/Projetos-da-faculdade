def calcular_z(x, y):
    z = ((x ** 2 + y ** 2) * (x - y) ** 2)  # Cálculo da fórmula
    return z

# Solicita os valores ao usuário
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

# Calcula e exibe o resultado
resultado = calcular_z(x, y)
print("O valor de z é:", resultado)

