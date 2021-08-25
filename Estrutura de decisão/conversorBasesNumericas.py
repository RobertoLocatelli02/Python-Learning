while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        opcao = int(input('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: '''))

        if(opcao == 1):
            print(f'{numero} convertido para BINARIO é igual a {bin(numero)[2:]}')
            break
        elif(opcao == 2):
            print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
            break
        elif(opcao == 3):
            print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
            break
        else:
            print('Opção inválida! Tente novamente.')
    except ValueError:
        print('Valor inserido não é válido! Por favor informe um número inteiro.')