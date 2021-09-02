num = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite mais um número: ")), int(input("Digite um último número: ")))
print(f'Você escolheu os números: {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na posição {num.index(3) + 1}')
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print("Os valores pares digitados foram: ", end = '')
for i in num:
    if i % 2 == 0:
        print(i, end = ' ')

