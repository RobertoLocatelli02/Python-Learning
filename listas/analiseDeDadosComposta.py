dados = []
pessoas = []
maiorPeso = None
menorPeso = None

while True:
    dados.clear()
    dados.append(input("Nome: ").strip().capitalize())
    dados.append(float(input("Peso: ")))

    if maiorPeso is None:
        maiorPeso = dados[1]
        menorPeso = dados[1]
    if dados[1] > maiorPeso:
        maiorPeso = dados[1]
    if dados[1] < menorPeso:
        menorPeso = dados[1]

    pessoas.append(dados[:])
    op = input('Deseja continuar?\n').strip().upper()
    if op != 'S':
        break
print(f'{len(pessoas)} pessoas foram cadastradas')
print(f'maior peso {maiorPeso} kg que é o peso de ', end = '')
for i in pessoas:
    if i[1] == maiorPeso:
        print(f'[{i[0]}] ', end = '')
print(f'\nmenor peso {menorPeso} kg que é o peso de ', end = '')
for i in pessoas:
    if i[1] == menorPeso:
        print(f'[{i[0]}] ', end = '')