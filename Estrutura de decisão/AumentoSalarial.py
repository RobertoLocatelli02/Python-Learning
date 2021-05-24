salario = float(input("Informe seu salário atual: R$"))
print(f"Salário antes do reajuste: R${salario}")
if salario <= 280:
    print(f"Valor do aumento: R${(salario * 0.20)}")
    salario += (salario * 0.20)
    print(f"Salário com reajuste de 20%: R${salario}")
elif salario <= 700:
    print(f"Valor do aumento: R${(salario * 0.15)}")
    salario += (salario * 0.15)
    print(f"Salário com reajuste de 15%: R${salario}")
elif salario <= 1500:
    print(f"Valor do aumento: R${(salario * 0.10)}")
    salario += (salario * 0.10)
    print(f"Salário com reajuste de 10%: R${salario}")
else:
    print(f"Valor do aumento: R${(salario * 0.05)}")
    salario += (salario * 0.05)
    print(f"Salário com reajuste de 5%: R${salario}")