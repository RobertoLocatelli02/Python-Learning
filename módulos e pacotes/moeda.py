from util import resumo


def pegaValorInicial():
    while True:
        valor = float(input("Digite o valor da moeda: "))
        if valor > 0:
            break
        print("Valor tem que ser maior que 0")
    return valor


def main():
    valor = pegaValorInicial()
    resumo(valor, 14, 33)


if __name__ == "__main__":
    main()