aluno = {}
aluno['nome'] = input("Nome: ").strip().capitalize()
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['media'] >= 7:
    aluno['resultado'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['resultado'] = 'Recuperação'
else:
    aluno['resultado'] = 'Reprovado'

for key, value in aluno.items():
    print(f'{key} = {value}')