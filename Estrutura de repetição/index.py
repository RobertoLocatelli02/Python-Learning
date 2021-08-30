j = 1
somaJ = 0
for i in range (30):
    print(f'{i}, {j} centavos')
    somaJ += j
    j *= 2
print(f'\n\n{somaJ}')