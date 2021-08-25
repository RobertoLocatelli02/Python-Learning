while True:
    try:
        numero1 = float(input('Informe um número: '))
        numero2 = float(input('Informe outro número: '))

        if numero1 > numero2:
            print(f'{numero1} > {numero2}')
        elif numero1 > numero2:
            print(f'{numero1} < {numero2}')
        else:
            print('Os números são iguais')
        break
    except ValueError:
        print('Valor inserido não é válido! Insira um valor numérico.')