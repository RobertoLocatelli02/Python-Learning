valor = int(input("Informe o valor de saque: "))
#478
notade100 = valor // 100 #478 // 10 = 4.78 -> 4
valor %= 100 #478 % 100 = 78
notade50 = valor // 50 #78 // 50 = 1.72 -> 1
valor %= 50 #78 % 50 = 28
notade10 = valor // 10 #28 // 10 = 3.8 -> 2
valor %= 10 #28 % 10 = 8
notade5 = valor // 5 #8 // 5 = 1.6 -> 1
notade1 = valor % 5 #8 % 5 = 3
print(f"{notade100} notas de 100 \n{notade50} notas de 50 \n{notade10} notas de 10 \n{notade5} notas de 5 \n{notade1} notas de 1")