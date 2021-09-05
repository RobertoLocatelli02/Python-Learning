pessoa = {}
pessoas = []
somaIdade = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input("Nome: ").strip().capitalize()
    while True:
        pessoa['sexo'] = input("Sexo: ").strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    pessoa['idade'] = int(input("Idade: "))
    somaIdade += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        op = input("Deseja continuar? ").strip().upper()
        if op[0] in 'SN':
            break
        print("ERRO! Responda Sim ou Não.")
    if op != 'S':
        break

media = somaIdade / len(pessoas)

print("-=" * 30)
print(pessoas)
print("-=" * 30)
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'A média de idade é de {media:.2f} anos.')
print(f'As mulheres cadastradas foram: ', end = '')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]} ', end = '')
print("\nlista das pessoas que estão acima da média de idade: ", end = '')
for pessoa in pessoas:
    if pessoa['idade'] > media:
        print(f'{pessoa["nome"]} ', end = '')