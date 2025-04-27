nome = input("digite seu nome: ")
sexo = input("digite seu sexo: ")
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

imc = peso/(altura * altura)
print(imc)

if (imc<=25) and (imc>18,6):
    print("você está normal")
elif (imc<=29,9) and (imc>25):
    print ("você está sobrepeso")
elif (imc<=18,5):
    print("você está abaixo do peso")
elif (imc<=39,9) and (imc>35):
    print("você está com obesidade de grau 2")
elif (imc<=30) and (imc>34,9):
    print("você está com obesidade de grau 1")
elif (imc<=40):
    print("você está com obesidade de grau 3")