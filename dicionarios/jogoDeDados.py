from random import randint
from time import sleep
from operator import itemgetter

ranking = []
resultado = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6)
}

for jogador, valor in resultado.items():
    print(f'O {jogador} tirou {valor} no dado')
    sleep(1)
ranking = sorted(resultado.items(), key = itemgetter(1), reverse = True)
print("-=" * 30)
print(f"{'RESULTADO':^60}")
print('-=' * 30)
for  posicao, resultado in enumerate(ranking):
    print(f'{posicao + 1}º lugar: {resultado[0]} com {resultado[1]}')
    sleep(1)