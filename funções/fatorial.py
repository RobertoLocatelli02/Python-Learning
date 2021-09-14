def calculaFatorial(numero, mostrarCalculo = True):
    fatorial = 1
    for i in range(numero, 0, -1):
        if mostrarCalculo:
            if i > 1:
                print(f'{i} x ', end = '')
            else:
                print(f'{i} = ', end = '')
        fatorial *= i
    return fatorial


def pegaValor():
    while True:
        try:
            numero = int(input("Digite o valor: "))
            if numero >= 0:
                return numero
            else:
                print('Digite um valor positivo!')
        except ValueError:
            print("Digite um valor inteiro!")


def main():
    valor = pegaValor()
    print(calculaFatorial(valor))


if __name__ == "__main__":
    main()