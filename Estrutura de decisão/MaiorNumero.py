num1 = float(input("Informe um número: "))
num2 = float(input("Informe um número: "))
num3 = float(input("Informe um número: "))
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
elif num3 > num1 and num3 > num2:
    maior = num3
print(f"O maior número é o {maior}")
