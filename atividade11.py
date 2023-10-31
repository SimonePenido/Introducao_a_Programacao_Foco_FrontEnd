def calculadora():
    while True:
        print("\nSelecione a operação desejada:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        operacao = int(input("Digite o número para a operação desejada: "))

        if operacao == 0:
            print("Saindo da calculadora.")
            break
        elif operacao not in [1, 2, 3, 4]:
            print("Essa opção não existe. Por favor, escolha uma opção válida.")
            continue

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == 1:
            print(f"O resultado da soma é: {num1 + num2}")
        elif operacao == 2:
            print(f"O resultado da subtração é: {num1 - num2}")
        elif operacao == 3:
            print(f"O resultado da multiplicação é: {num1 * num2}")
        elif operacao == 4:
            if num2 != 0:  # Evita divisão por zero
                print(f"O resultado da divisão é: {num1 / num2}")
            else:
                print("Erro: divisão por zero. Por favor, tente novamente.")

calculadora()
