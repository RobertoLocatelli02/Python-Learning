lista = []
while True:
    num = int(input("Digite um número: "))
    if lista.__contains__(num):
        print("Número já informado!")
    else:
        lista.append(num)
    op = input("Deseja continuar?\n").strip().upper()
    if op != "S":
        break
lista.sort()
print(f"Os valores digitados em ordem crescente: {lista}")