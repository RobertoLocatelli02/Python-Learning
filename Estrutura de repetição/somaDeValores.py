cont = 0
soma = 0

while True:
    numero = int(input("Digite um número: "))
    if numero == 999:
        break
    else:
        cont += 1
        soma += numero

print(f"""Total de jogadas: {cont}
Soma dos números inseridos: {soma}""")
