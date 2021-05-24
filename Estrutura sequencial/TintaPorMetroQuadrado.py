import math
metrosQuadrados = float(input("Informe quantos metros quadrados serão pintados: "))
litrosTinta = metrosQuadrados / 3
latasTinta = math.ceil(litrosTinta / 18)
totalAPagar = latasTinta * 80
print(f"Metros quadrados a serem pintados: {metrosQuadrados} \nLitros de tinta a serem precisos: {litrosTinta} \nQuantidade de latas de tinta que serão usadas: {latasTinta} \nTotal a pagar: R${totalAPagar}")