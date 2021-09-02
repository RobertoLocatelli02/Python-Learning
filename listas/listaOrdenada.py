lista = []
for i in range(5):
    numero = int(input("Digite um valor: "))
    if i == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista')
                break
            posicao += 1
print("-=" * 30)
print(f'Os valores digitados em ordem foram: {lista}')