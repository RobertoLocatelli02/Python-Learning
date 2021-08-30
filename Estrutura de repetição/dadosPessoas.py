idadeMaisVelho = 0
contMulheres = 0
somaIdade = 0

for i in range(4):
    nome = input('Informe seu nome: ').capitalize()
    idade = int(input('Informe sua idade: '))
    sexo = input('Informe seu sexo: ').capitalize()
    print()

    if idade > idadeMaisVelho and sexo == "Masculino":
        idadeMaisVelho = idade
        nomeMaisVelho = nome
    if sexo == "Feminino" and idade < 20:
        contMulheres += 1

    somaIdade += idade

mediaIdade = somaIdade / 4

print(f'''Média geral de idade: {mediaIdade} anos
Nome do homem mais velho: {nomeMaisVelho}
{contMulheres} mulher(es) tem menos de 20 anos''')