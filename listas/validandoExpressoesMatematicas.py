expressao = input('Digite a expressão: ')
lista = []
for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')