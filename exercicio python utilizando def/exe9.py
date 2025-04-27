def repetir_mensagem():
    mensagem = input("Digite a mensagem: ")
    n = int(input("Quantas vezes deseja repetir? "))
    
    for _ in range(n):
        print(mensagem)


repetir_mensagem()