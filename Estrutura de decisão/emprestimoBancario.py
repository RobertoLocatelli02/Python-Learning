valorCasa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o valor do salário: R$'))
quantidadeAnos = int(input('Em quantos anos pagará a casa?\n'))

valorPrestacao = valorCasa / quantidadeAnos
if valorPrestacao > salario * 0.3:
    print('Empréstimo negado!')
else:
    print('Empréstimo realizado!')