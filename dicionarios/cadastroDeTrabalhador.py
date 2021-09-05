from datetime import datetime

dados = {}
dados['nome'] = input("Nome: ").strip().capitalize()
nascimento = int(input("Ano de nascimento: "))
dados['idade'] = datetime.now().year - nascimento
dados['carteira'] = int(input("Carteira de trabalho (0 se não tenha): "))
if dados['carteira'] != 0:
    dados['contratacao'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salário: R$"))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print("-=" * 30)
for key, value in dados.items():
    print(f'{key} tem o valor {value}')