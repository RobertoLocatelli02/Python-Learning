try:
    valor = float(input('Informe o valor a ser pago: R$'))
    if valor <= 0:
        print("Valor inserido não é válido!")
    else:
        opcao = int(input('''Insira a opção da forma de pagamento:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão
Sua opção: '''))
        if opcao == 1:
            print(f'Valor original: R${valor}\nValor com 10% de desconto: R${valor - (valor * 0.1)}')
        elif opcao == 2:
            print(f'Valor original: R${valor}\nValor com 5% de desconto: R${valor - (valor * 0.05)}')
        elif opcao == 3:
            print(f'Valor total a ser pago: R${valor}\nValor de cada parcela: R${round((valor / 2),2)}')
        elif opcao == 4:
            print(f'Valot total a ser pago com 20% de juros: R${valor}\nValor de cada parcela: R${round((valor / 3),2)}')
        else:
            print('Opção invalida!')
except ValueError:
    print("Valor inserido não é válido!")