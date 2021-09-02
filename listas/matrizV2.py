matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = 0
maiorValor = None
somaColuna = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print("-=" * 30)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end = '')
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]

        if matriz[linha][coluna] == matriz[linha][2]:
            somaColuna += matriz[linha][coluna]

        if maiorValor is None:
            maiorValor = matriz[1][coluna]
        
        if matriz[1][coluna] > maiorValor:
            maiorValor = matriz[1][coluna]
    print()
print("-=" * 30)
print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaColuna}')
print(f'O maior valor da segunda linha é {maiorValor}')