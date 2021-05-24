turno = str(input("Qual turno você estuda? \n")).strip().lower()
if turno == "matutino":
    print("Bom dia!")
elif turno == "vespertino":
    print("Boa tarde!")
elif turno == "noite":
    print("Boa noite!")
else:
    print("Valor inválido!")