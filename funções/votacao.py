from datetime import date

anoAtual = date.today().year


def voto(ano):
    idade = anoAtual - ano
    if idade < 16:
        return f'Com {idade} anos, a pessoa não vota ainda'
    elif idade >= 16 and idade < 18:
        return f'Com {idade} anos, o voto torna-se opcional'
    else:
        return f'Com {idade} anos, o voto é obrigatório'


def pegaAnoValido():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento: "))
            if ano > anoAtual:
                print(f"Ano não pode ser maior do que {anoAtual}")
            else:
                return ano
        except ValueError:
            print("Ano tem que ser um valor inteiro!")


def main():
    ano = pegaAnoValido()
    print(voto(ano))


if __name__ == "__main__":
    main()