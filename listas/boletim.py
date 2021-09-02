dados = []

while True:
    nome = input("Nome: ").strip().capitalize()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    op = input("Deseja continuar? ").strip().upper()
    if op != 'S':
        break
print("-=" * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-=" * 30)
for i, aluno in enumerate(dados):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-' * 30)
    op = int(input("Mostrar nota de qual aluno? (999 interrompe): "))
    if op == 999:
        print('FINALIZANDO...')
        break
    if op <= (len(dados) - 1):
        print(f'Notas de {dados[op][0]} são {dados[op][1]}')