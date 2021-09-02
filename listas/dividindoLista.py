lista = []
listaPar = []
listaImpar = []

while True:
    lista.append(int(input("Digite um número: ")))
    op = input('Deseja continuar?\n').strip().upper()
    if op != 'S':
        break

for i in lista:
    if i % 2 == 0:
        listaPar.append(i)
    else:
        listaImpar.append(i)

print("-=" * 30)
print(f'Lista dos números inseridos: {lista}')
print(f'Lista dos números pares: {listaPar}')
print(f'Lista dos impares: {listaImpar}')
print("-=" * 30)