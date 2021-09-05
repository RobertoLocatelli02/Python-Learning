jogador = {}
partidas = []
jogador['nome'] = input("Nome do jogador: ").strip().capitalize()
totalPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(totalPartidas):
    partidas.append(int(input(f'Quantos gols fez na {i + 1}º partida? ')))
jogador['gols'] = partidas[:]
jogador['totalGols'] = sum(partidas)

print('-=' * 30)
print(jogador)
print("-=" * 30)

for key, value in jogador.items():
    print(f'{key} tem valor {value}')
print("-=" * 30)
print(f'O jogador {jogador["nome"]} jogou {len(partidas)} partidas.')
for partida, totGols in enumerate(jogador['gols']):
    print(f'-> na partida {partida + 1}, fez {totGols} gols')
print(f'Foi um total de {jogador["totalGols"]} gols')