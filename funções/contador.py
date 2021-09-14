def contador(inicio, fim, passo):
    if inicio < fim:
        contador = inicio
        while contador <= fim:
            print(contador, end = ' ')
            contador += passo
    else:
        contador = inicio
        while contador >= fim:
            print(contador, end = ' ')
            contador -= passo

def pegaValores():
    while True:
        try:
            inicio = int(input("Digite o valor inicial: "))
        except ValueError:
            print("Valor inserido não é válido! Insira um numero inteiro.")
        try:
            fim = int(input("Digite o valor final: "))
        except ValueError:
            print("Valor inserido não é válido! Insira um numero inteiro.")
        try:
            passo = int(input("Digite o incremento: "))
            break
        except ValueError:
            print("Valor inserido não é válido! Insira um numero inteiro.")
    return inicio, fim, passo


def main():
    inicio, fim, passo = pegaValores()
    contador(inicio, fim, passo)


if __name__ == "__main__":
    main()