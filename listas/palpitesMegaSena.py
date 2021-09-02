from random import randint
from time import sleep

lista = []
jogos = []
cont = 0
totalJogos = 1
quant = int(input("Quantos jogos você quer que eu sorteie? "))
while totalJogos <= quant:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totalJogos += 1
print("-=" * 30)
print(f"{'Resultado':^30}")
print('-=' * 30)
for i, resultado in enumerate(jogos):
    print(f'Jogo {i + 1}: {resultado}')
    sleep(1)