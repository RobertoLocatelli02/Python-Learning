a1 = 0
a2 = 1
n = int(input('Quantos termos de Fibonacci você quer ver?\n'))
print(f'{a1} -> {a2}', end = '')
cont = 3
while cont <= n:
    an = a1 + a2
    print(f' -> {an}', end = '')
    a1 = a2
    a2 = an
    cont += 1
print(' -> FIM')