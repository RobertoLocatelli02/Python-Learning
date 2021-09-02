lista = []
while True:
    lista.append(int(input("Digite um número: ")))
    op = input('Deseja continuar?\n').strip().upper()
    if op != 'S':
        break
print(f'{len(lista)} números foram inseridos na lista')
lista.sort(reverse = True)
print(f'lista em ordem decrescente: {lista}')
if 5 in lista:
    print("O número 5 foi inserido na lista")
else:
    print("O número 5 não foi inserido na lista")