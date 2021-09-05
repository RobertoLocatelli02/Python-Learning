dados = {}
time = []
partidas = []

while True:
    dados.clear()
    partidas.clear()
    dados['nome'] = input("Nome: ").strip().capitalize()
    quantPartidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))
    for i in range(quantPartidas):
        partidas.append(int(input(f'Quantidade de gols na partida {i + 1}: ')))
    dados['gols'] = partidas[:]
    dados['totalGols'] = sum(dados['gols'])
    time.append(dados.copy())
    while True:
        op = input("Deseja continuar cadastrando jogadores? ").strip().upper()
        if op[0] == "S" or op[0] == "N":
            break
        print("Responda apenas sim ou não!")
    if op == "N":
        break

print("-=" * 30)
for key, value in enumerate(time):
    print(f'{key:>4} ', end = '')
    for dado in value.values():
        print(f'{str(dado):<15} ', end = '')
    print()

"""print('-=' * 30)
print(dados)
print("-=" * 30)

for key, value in dados.items():
    print(f'{key} tem valor {value}')
print("-=" * 30)
print(f'O jogador {dados["nome"]} jogou {len(partidas)} partidas.')
for partida, totGols in enumerate(dados['gols']):
    print(f'-> na partida {partida + 1}, fez {totGols} gols')
print(f'Foi um total de {dados["totalGols"]} gols')"""