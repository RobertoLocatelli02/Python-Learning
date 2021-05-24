peso = float(input("Informe quantos quilos de peixe foram trazidos: "))
if peso >= 0 and peso <= 50:
    print(f"{peso}kg está dentro do estabelecido pelo regulamento de pesca do Estado de São Paulo")
elif peso >= 51:
    excesso = peso - 50
    print(f"{peso}kg excedeu em {excesso}kg do permitido pelo regulamento! Valor da multa: R${excesso * 4}")
