frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
palavrasJuntas = ''.join(palavras)
inverso = ''

for i in range(len(palavrasJuntas) - 1, -1, -1):
    inverso += palavrasJuntas[i]
print(palavrasJuntas, inverso)

if inverso == palavrasJuntas:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
