ganhosPorHora = float(input("Informe a quantidade ganha por hora: R$"))
horasTrabalhadas = int(input("Informe quantas horas foram trabalhadas: "))
salarioBruto = ganhosPorHora * horasTrabalhadas
if salarioBruto <= 900:
    print(f"Salario bruto: R${salarioBruto} \n-IR (0%): R$0.00 \n-INSS (10%): R${(salarioBruto * 0.10)} \nFGTS (11%): R${(salarioBruto * 0.11)} \nTotal descontos: {(salarioBruto * 0.11) - (salarioBruto * 0.10)} \nSalário líquido: R${salarioBruto + (salarioBruto * 0.11) - (salarioBruto * 0.10)}")
elif salarioBruto <= 1500:
    print(f"Salario bruto: R${salarioBruto} \n-IR (5%): R${(salarioBruto * 0.05)} \n-INSS (10%): R${(salarioBruto * 0.10)} \nFGTS (11%): R${(salarioBruto * 0.11)} \nTotal descontos: {(salarioBruto * 0.11) - (salarioBruto * 0.10) - (salarioBruto * 0.05)} \nSalário líquido: R${salarioBruto + (salarioBruto * 0.11) - (salarioBruto * 0.10) - (salarioBruto * 0.05)}")
elif salarioBruto  <= 2500:
    print(f"Salario bruto: R${salarioBruto} \n-IR (10%): R${(salarioBruto * 0.10)} \n-INSS (10%): R${(salarioBruto * 0.10)} \nFGTS (11%): R${(salarioBruto * 0.11)} \nTotal descontos: {(salarioBruto * 0.11) - (salarioBruto * 0.10) - (salarioBruto * 0.10)} \nSalário líquido: R${salarioBruto + (salarioBruto * 0.11) - (salarioBruto * 0.10) - (salarioBruto * 0.10)}")
else:
    print(f"Salario bruto: R${salarioBruto} \n-IR (20%): R${(salarioBruto * 0.20)} \n-INSS (10%): R${(salarioBruto * 0.10)} \nFGTS (11%): R${(salarioBruto * 0.11)} \nTotal descontos: {(salarioBruto * 0.11) - (salarioBruto * 0.10) - (salarioBruto * 0.20)} \nSalário líquido: R${salarioBruto + (salarioBruto * 0.11) - (salarioBruto * 0.10) - (salarioBruto * 0.20)}")