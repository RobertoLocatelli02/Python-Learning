cont = 0
pergunta = str(input("Telefonou para a vítima?\n")).strip().lower()
if pergunta[0] == "s":
    cont += 1
pergunta = str(input("Esteve no local do crime?\n")).strip().lower()
if pergunta[0] == "s":
    cont += 1
pergunta = str(input("Mora perto da vítima?\n")).strip().lower()
if pergunta[0] == "s":
    cont += 1
pergunta = str(input("Devia para a vítima?\n")).strip().lower()
if pergunta[0] == "s":
    cont += 1
pergunta = str(input("Já trabalhou com a vítima?\n")).strip().lower()
if pergunta[0] == "s":
    cont += 1

if cont == 2:
    print("Suspeita")
elif cont == 3 or cont == 4:
    print("Cúmplice")
elif cont == 5:
    print("Assassino")
else:
    print("Inocente")