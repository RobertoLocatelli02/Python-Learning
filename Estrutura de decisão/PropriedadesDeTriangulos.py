lado1 = float(input("Informe um dos lados do triangulo: "))
lado2 = float(input("Informe um outro lado do triangulo: "))
lado3 = float(input("Informe o último lado do triângulo: "))
if lado1 == lado2 == lado3:
    print("Triangulo equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triangulo isósceles")
else:
    print("Triangulo escaleno")