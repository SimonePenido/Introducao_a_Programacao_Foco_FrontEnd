def calcular_idade(nome, ano_nascimento):
    ano_atual = 2023
    idade = ano_atual - ano_nascimento
    print(f"Olá {nome}, você completou ou irá completar {idade} anos neste ano!")

def receber_entrada():
    while True:
        nome = input("Por favor, insira seu nome completo: ")
        try:
            ano_nascimento = int(input("Insira seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2022:
                calcular_idade(nome, ano_nascimento)
                break
            else:
                print("O ano de nascimento deve estar entre 1922 e 2021. Por favor, tente novamente.")
        except ValueError:
            print("Erro: Insira um valor numérico para o ano de nascimento. Por favor, tente novamente.")

receber_entrada()
