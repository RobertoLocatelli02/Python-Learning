try:
    idade = int(input('Informe a idade do atleta: '))
    if idade <= 0:
        print('Idade informada não é válida.')
    elif idade <= 9:
        print(f'Com {idade} anos, o atleta encontra-se na categoria MIRIM')
    elif idade <= 14:
        print(f'Com {idade} anos, o atleta encontra-se na categoria INFATIL')
    elif idade <= 19:
        print(f'Com {idade} anos, o atleta encontra-se na categoria JÚNIOR')
    elif idade <= 25:
        print(f'Com {idade} anos, o atleta encontra-se na categoria SÊNIOR')
    else:
        print(f'Com {idade} anos, o atleta encontra-se na categoria MASTER')
except ValueError:
    print('Valor inserido não é válido! Insira um valor inteiro')