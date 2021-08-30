a1 = float(input('Informe o primeiro termo da PA: '))
razao = float(input('Informe a razão da PA: '))

for i in range(1, 11):
    an = a1 + ((i - 1) * razao)
    print(an)