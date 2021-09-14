def maiorNumero(numeros):
    print(f'O maior número entre {numeros} é {max(numeros)}')


def pegaNumeros():
    numeros = []
    while True:
        numero = float(input("Digite um número: "))
        numeros.append(numero)
        op = input("Deseja continuar?\n").strip().upper()
        if op == "N":
            break
    return numeros


def main():
    numeros = []
    numeros = pegaNumeros()
    maiorNumero(numeros)


if __name__ == "__main__":
    main()