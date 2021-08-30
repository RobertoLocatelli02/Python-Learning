cont = 0

for i in range(7):
    ano = int(input('Informe o ano de nascimento: '))
    if ano <= 2003:
        cont += 1
print(f'{cont} pessoas são maiores de idade')