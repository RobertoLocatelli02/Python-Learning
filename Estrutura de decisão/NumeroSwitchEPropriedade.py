import math
num1 = float(input("Informe um número: "))
num2 = float(input("Informe um número: "))
op = int(input("Menu de opções: \n1: soma\n2: subtração \n3: multiplicação \n4: divisão \n5: potenciação \n6: raiz quadrada \nOpção: "))

if op == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == 2:
    op1 = int(input(f"Menu de opções: \n1: {num1} - {num2} \n2: {num2} - {num1} \nOpção: "))
    if op1 == 1:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif op1 == 2:
        print(f"{num2} - {num1} = {num2 - num1}")
    else:
        print("valor digitado inválido")
elif op == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == 4:
    op1 = int(input(f"Menu de opções: \n1: {num1} / {num2} \n2: {num2} / {num1} \nOpção: "))
    if op1 == 1:
        print(f"{num1} / {num2} = {num1 / num2}")
    elif op1 == 2:
        print(f"{num2} / {num1} = {num2 / num1}")
    else:
        print("valor digitado inválido")
elif op == 5:
    op1 = int(input(f"Menu de opções: \n1: {num1} ^ {num2} \n2: {num2} ^ {num1} \nOpção: "))
    if op1 == 1:
        print(f"{num1} ^ {num2} = {math.pow(num1,num2)}")
    elif op1 == 2:
        print(f"{num2} ^ {num1} = {math.pow(num2,num1)}")
    else:
        print("valor digitado inválido")
elif op == 6:
    op1 = int(input(f"Menu de opções: \n1: √{num1} \n2: √{num2} \nOpção: "))
    if op1 == 1:
        print(f"√{num1} = {math.sqrt(num1)}")
    elif op1 == 2:
        print(f"√{num2} = {math.sqrt(num2)}")
    else:
        print("valor digitado inválido")
else:
    print("valor digitado inválido")