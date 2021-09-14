from random import randint

def sorteiaNumeros():
    numeros = [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]
    print(f"Os números sorteados foram: {numeros}")
    return numeros


def somaPar(numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f"A soma dos números pares na lista {numeros} é igual à {soma}")


def main():
    numeros = sorteiaNumeros()
    print(numeros)
    somaPar(numeros)

if __name__ == "__main__":
    main()