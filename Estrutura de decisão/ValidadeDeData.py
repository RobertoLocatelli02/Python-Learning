dd = int(input("dd/MM/aaaa \ndd: "))
mm = int(input("mm: "))
aaaa = int(input("aaaa: "))
if dd >= 1 and dd <= 30 and mm >= 1 and mm <= 12 and aaaa >= 0:
    print(f"{dd}/{mm}/{aaaa} é uma data valida")
else:
    print(f"{dd}/{mm}/{aaaa} não é uma data valida")