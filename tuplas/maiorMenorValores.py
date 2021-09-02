import random

lista = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
print(f'Numeros sorteados: {lista}')

print(f'maior numero sorteado: {max(lista)}\nmenor numero sorteado: {min(lista)}')