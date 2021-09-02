numero = int(input("Informe o número: "))
if numero > 0:
    numeroAntigo = numero
    resultado = numero

    while numero != 1:
        numero -= 1
        resultado *= numero

    print(f'{numeroAntigo}! = {resultado}')
else:
    print("Número informado não é válido! Insira um valor positivo.")