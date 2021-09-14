def ficha(nome, quantidadeGols):
    print(f"O jogador {nome} fez {quantidadeGols} gols no campeonato")


def pegaNomeJogador():
    nome = input("Digite o nome do jogador: ")
    if nome.strip() == '':
        nome = "<desconhecido>"
    return nome


def pegaQuantidadeDeGols():
    quantGols = input("Digite a quantidade de gols feitos: ")
    if quantGols.isnumeric():
        quantGols = int(quantGols)
    else:
        quantGols = 0
    return quantGols

def main():
    nome = pegaNomeJogador()
    gols = pegaQuantidadeDeGols()
    ficha(nome, gols)

if __name__ == "__main__":
    main()