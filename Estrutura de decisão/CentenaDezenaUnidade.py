numero = int(input("Informe um número: "))
#1729
unidade = int(numero % 10) # 1729 % 10 = 9
numero = (numero - unidade) / 10 #1729 - 9 = 1720 / 10 = 172 
dezena = int(numero % 10) #172 % 10 = 2
numero = (numero - dezena) / 10 #172 - 2 = 170 / 10 = 17
centena = int(numero % 10) #17 % 10 = 7
milhar = int((numero - centena) / 10) #17 - 7 = 10 / 10 = 1
print(f"milhar: {milhar} \ncentena: {centena} \ndezena: {dezena} \nunidade: {unidade}") 