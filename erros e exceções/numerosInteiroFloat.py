def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print("ERRO: digite um número inteiro válido.")
        else:
            return numero


def leiaFloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except (ValueError, TypeError):
            print("ERRO: digite um valor numérico válido.")
        else:
            return numero


def response(numInt, numFloat):
    print(f'O numero inteiro digitado foi {numInt}\nO numero real digitado foi {numFloat}')

def main():
    numeroInt = leiaInt("Digite um numero inteiro: ")
    numeroFloat = leiaFloat("Digite um numero real: ")
    response(numeroInt, numeroFloat)


if __name__ == "__main__":
    main()