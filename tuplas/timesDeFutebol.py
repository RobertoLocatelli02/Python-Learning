times = ("Atlético-MG", "Palmeiras", "Fortaleza EC", "Bragantino", "Flamengo", "Corinthians", "Atlético Goianiense",
        "Ceará", "Athletico-PR", "Internacional", "Santos", "São Paulo", "Fluminense", "Juventude", "Cuiabá", "Bahia",
        "América-MG", "Grêmio", "Sport", "Chapecoense")

print("=-" * 100)
print("Lista do brasileirão: ")
print(times)
print("=-" * 100)

print(f"Os 5 primeiros: {times[:5]}")
print(f'Os últimos 4 colocados: {times[16:]}')
print(f'Chapecoense está na posição {times.index("Chapecoense") + 1}')

print("=-" * 100)
print("Times em ordem alfabética: ")
print(sorted(times))
print("=-" * 100)