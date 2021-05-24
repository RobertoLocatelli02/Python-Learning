import math
a = float(input("ax² + bx + c \na = "))
if a == 0:
    print("A equação não é do segundo grau")
else:
    b = float(input("b = "))
    c = float(input("c = "))

    delta = (math.pow(b,2) - (4 * a * c))
    if delta < 0:
        print("A equação não possui raizes reais")
    elif delta == 0:
        print("A equação possui apenas uma raiz real")
    else:
        print("A equação possui duas raizes reais")