try:
    nota1 = float(input('Informe a nota da primeira prova: '))
    if nota1 < 0 or nota1 > 10:
        print('Digite um valor entre 0 e 10.')
    else:
        nota2 = float(input('Informe a nota da segunda prova: '))
        if nota2 < 0 or nota2 > 10:
            print('Digite um valor entre 0 e 10.')
        else:
            media = round(((nota1 + nota2) / 2),2)
            if media >= 7:
                print(f'Aluno aprovado com média {media}')
            elif media >= 5 and media < 7:
                print(f'Aluno de recuperação com média {media}')
            else:
                print(f'Aluno reprovado com média {media}')
except ValueError as e:
    print('Valor inserido não é válido! Insira um valor numérico.')