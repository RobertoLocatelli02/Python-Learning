def areaDoRetangulo(largura, comprimento):
    print(f'ÁREA DO RETÂNGULO {largura} x {comprimento} = {largura * comprimento}')


def pegaValoresValidos():
    while True:
        try:
            largura = float(input("Digite a largura: "))
            if largura > 0:
                break
            else:
                print("Insira um valor positivo.")
        except ValueError:
            print("Valor inserido não é válido! Insira um valor numérico.")
    while True:
        try:
            comprimento = float(input("Digite o comprimento: "))
            if comprimento > 0:
                break
            else:
                print("Insira um valor positivo.")
        except ValueError:
            print("Valor inserido não é válido! Insira um valor numérico.")
    return largura, comprimento


def main():
    largura, comprimento = pegaValoresValidos()
    areaDoRetangulo(largura, comprimento)

if __name__ == "__main__":
    main()