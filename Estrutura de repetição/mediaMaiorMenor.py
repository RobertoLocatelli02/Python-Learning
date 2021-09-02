numero = float(input('Informe um número: '))
menor = maior = numero
soma = cont = 0

while True:
    try:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        soma += numero
        cont += 1
        op = input("Você deseja continuar?\n").strip().upper()
        if op[0] == "N":
            break
        elif op[0] == "S":
            numero = float(input('Informe um número: '))
        else:
            print("Digite \"sim\" ou \"não\"!")
            break
    except ValueError:
        print("Valor inserido não é válido! Insira um valor numérico.")
print(f'''maior número = {maior}
menor número = {menor}
média dos números informados = {soma / cont}''')