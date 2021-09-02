lista = (input("Digite uma palavra: ").lower(), input("Digite uma palavra: ").lower(),
        input("Digite uma palavra: ").lower(), input("Digite uma palavra: ").lower(), 
        input("Digite uma palavra: ").lower(), input("Digite uma palavra: ").lower(), 
        input("Digite uma palavra: ").lower(), input("Digite uma palavra: ").lower())

for i in lista:
    print(f'\nNa palavra {i.upper()} temos as vogais ', end = '')
    for letra in i:
        if letra in "aeiou": #sem acentuação
            print(letra.upper(), end = ' ')