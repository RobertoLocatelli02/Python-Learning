numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))

while True:
    menu = int(input("""\nMenu de opções:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
sua opção: """))
    if menu == 1:
        print(f'{numero1} + {numero2} = {numero1 + numero2}\n')
    elif menu == 2:
        print(f'{numero1} * {numero2} = {numero1 * numero2}\n')
    elif menu == 3:
        if numero1 > numero2:
            print(f'{numero1} > {numero2}\n')
        elif numero1 < numero2:
            print(f'{numero2} > {numero1}\n')
        else:
            print(f'{numero1} == {numero2}\n')
    elif menu == 4:
        numero1 = float(input("Informe o primeiro número: "))
        numero2 = float(input("Informe o segundo número: "))
        print()
    elif menu == 5:
        break
    else:
        print("Opção inválida! Escolha uma das opções entre 1 e 5.")