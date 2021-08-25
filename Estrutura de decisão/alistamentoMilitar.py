import datetime

dataAtual = datetime.datetime.now()
data = dataAtual.date()
ano = int(data.strftime("%Y"))

try:
    anoNascimento = int(input('Informe o ano de nascimento: '))
    if ((ano - anoNascimento) > 18):
        print(f'Você já deveria ter se alistado em {anoNascimento + 18}')
    elif ((ano - anoNascimento) < 18):
        print(f'Voce só vai precisar se alistar em {anoNascimento + 18}')
    else:
        print(f'Está no seu ano de alistamento.')
except ValueError:
    print('Valor inserido não é válido! Insira um valor inteiro')