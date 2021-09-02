cont1000 = 0
somaValor = 0
nomeBarato = None
precoBarato = None

while True:
    nome = input('Nome do produto: ').strip().capitalize()
    preco = float(input('Preço do produto: R$'))
    somaValor += preco
    if preco >= 1000:
        cont1000 += 1
    if precoBarato is None:
        precoBarato = preco
        nomeBarato = nome
    if preco < precoBarato:
        precoBarato = preco
        nomeBarato = nome
    op = input("Deseja continuar? ").strip().upper()
    if op[0] != "S":
        break
print(f"""total gasto: R${somaValor}
{cont1000} produtos custam mais do que R$1000
{nomeBarato} é o produto mais barato e custa {precoBarato}""")