a1 = float(input('Informe o primeiro termo da PA: '))
razao = float(input('Informe a razão da PA: '))
termo = a1
i = 1
total = 0
mais = 10

while True:
    total += mais
    while i <= total:
        print(f'{termo} -> ', end = '')
        termo += razao
        i += 1
    print("PAUSA")
    mais = int(input("Deseja ver mais quantos termos?\n"))
    if mais == 0:
        break
print(f'Progressão finalizada com {total} termos mostrados')