import random

palpites = 0
while True:
    try:
        numero = int(input("Informe um número entre 0 e 10: "))
        if numero >= 0 and numero <= 10:
            numeroAleatorio = random.randint(0, 10)
            palpites += 1
            if numero == numeroAleatorio:
                break
            else:
                print("Tente novamente!")
        else:
            print('Insira um valor entre 0 e 10.')
    except ValueError:
        print("Valor inserido não é válido! Insira um valor inteiro entre 0 e 10.")
print(f'Você acertou e teve um total de {palpites} tentativas')