import random

cont = 0
while True:
    ("-" * 20)
    numero = int(input("Informe um número: "))
    op = input("Você quer ser par ou ímpar? ").strip().upper()
    numeroAleatorio = random.randint(0, 10)
    print(f'Você jogou {numero} e o computador jogou {numeroAleatorio}')
    soma = numero + numeroAleatorio
    if op == "P":
        if soma % 2 == 0:
            print("Você venceu!")
            cont += 1
        elif soma % 2 == 1:
            print("Você perdeu")
            break
    if op == "I":
        if soma % 2 == 1:
            print('Você venceu!')
            cont += 1
        elif soma % 2 == 0:
            print('Você perdeu!')
            break
print("-" * 20)
print(f'GAME OVER! Você ganhou {cont} rodadas.')
print("-" * 20)
