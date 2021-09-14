def escreva(mensagem):
    print("~" * len(mensagem))
    print(mensagem)
    print("~" * len(mensagem))

def pegaMensagem():
    mensagem = input("Digite aqui a mensagem: ").strip().upper()
    return mensagem


def main():
    mensagem = pegaMensagem()
    escreva(mensagem)


if __name__ == "__main__":
    main()