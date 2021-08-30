somaNum = 0
for i in range(6):
    num = float(input("Informe um número: "))
    if num % 2 == 0:
        somaNum += num
print(somaNum)