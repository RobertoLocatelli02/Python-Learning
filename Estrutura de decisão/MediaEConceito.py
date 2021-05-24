nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 9 and media <= 10:
    print("Conceito A")
elif media >= 7.5 and media < 9:
    print("Conceito B")
elif media >= 6 and media < 7.5:
    print("Conceito C")
elif media>= 4 and media < 6:
    print("Conceito D")
elif media >= 0 and media < 4:
    print("Conceito E")
else:
    print("Valor invalido!")

if media >= 6 and media <= 10:
    print("Aluno aprovado")
elif media >= 0 and media < 6:
    print("Aluno reprovado")