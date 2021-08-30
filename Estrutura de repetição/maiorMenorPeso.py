maiorPeso = 0
menorPeso = 1000000

for i in range(5):
    peso = float(input('Informe seu peso: '))
    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso
print(f'''maior peso: {maiorPeso} kg
menor peso: {menorPeso} kg''')