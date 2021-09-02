a1 = float(input('Informe o primeiro termo da PA: '))
razao = float(input('Informe a razão da PA: '))
i = 1

while i != 11:
    an = a1 + ((i - 1) * razao)
    i += 1
    print(an)