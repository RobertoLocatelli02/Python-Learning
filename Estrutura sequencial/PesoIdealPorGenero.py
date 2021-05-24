sexo = str(input("Informe o sexo: ")).strip().lower()
altura = float(input("Informe a altura: "))
if sexo[0] == "m":
    print(f"Cálculo do peso ideal para homens: (72.7 * {altura}) - 58 = {(72.7 * altura) - 58}")
if sexo[0] == "f":
    print(f"Cálculo do peso ideal para mulheres: (62.1 * {altura}) - 44.7 = {(62.1 * altura) - 44.7}")