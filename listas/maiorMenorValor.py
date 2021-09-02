lista = []

for i in range(5):
    lista.append(int(input(f"Digite um número para a posição {i + 1}: ")))

print(f'maior valor encontrado foi {max(lista)} e está nas posições ', end = '')
for i, num in enumerate(lista):
    if num == max(lista):
        print(f'{i + 1}... ', end = '')

print(f'\nmenor valor encontrado foi {min(lista)} e está nas posições ', end = '')
for i, num in enumerate(lista):
    if num == min(lista):
        print(f'{i + 1}... ', end = '')