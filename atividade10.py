def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:  # Evitar divisão por zero
            return num1 / num2
        else:
            print("Erro: divisão por zero.")
            return 0
    else:
        print("Operação não reconhecida.")
        return 0

# Exemplo de uso da função
resultado = calculadora(6, 3, 2)  # Exemplo de subtração
print("O resultado da operação é:", resultado)
