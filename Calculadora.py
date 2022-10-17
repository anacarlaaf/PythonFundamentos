print("____________________Python Calculator____________________")

while True:
    print("\nSelecione a operação desejada: \n")
    print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n")
    opcao = (input("Digite sua opção (1/2/3/4): "))

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    if opcao == "1":
        resultado = numero1 + numero2
        print("%.2f + %.2f = %.2f" % (numero1, numero2, resultado))
        break
    elif opcao == "2":
        resultado = numero1 - numero2
        print("%.2f - %.2f = %.2f" % (numero1, numero2, resultado))
        break
    elif opcao == "3":
        resultado = numero1*numero2
        print("%.2f x %.2f = %.2f" % (numero1, numero2, resultado))
        break
    elif opcao == "4":
        resultado = numero1/numero2
        print("%.2f / %.2f = %.2f" % (numero1, numero2, resultado))
        break
    else:
        print("\nOpção inválida. Tente novamente.")
