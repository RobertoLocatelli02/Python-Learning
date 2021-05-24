ganhosPorHora = float(input("Informe os ganhos por hora: R$"))
horasTrabalhadas = int(input("Informe o total de horas trabalhadas: "))
salarioBruto = ganhosPorHora * horasTrabalhadas
print(f"+Salario bruto: {salarioBruto} \n-INSS(8%): {(salarioBruto * 0.08)} \n-Sindicato(5%): {(salarioBruto * 0.05)} \n-Imposto de Renda(11%): {(salarioBruto * 0.11)} \nSalario líquido: {salarioBruto + (- (salarioBruto * 0.08) - (salarioBruto * 0.05) - (salarioBruto * 0.11))}")