def metade(valor):
    return valor / 2


def dobrar(valor):
    return valor * 2


def aumentar(valor, aumento):
    return valor + (valor * (aumento / 100))


def diminuir(valor, reducao):
    return valor - (valor * (reducao / 100))


def formatarMoeda(valor, show = True):
    if show:
        return "R${:.2f}".format(valor)
    else:
        return valor

def resumo(valor, aumento, reducao):
    print("-" * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print("-" * 30)
    print(f'''Preço analisado: {formatarMoeda(valor)}
Dobro do preço: {formatarMoeda(dobrar(valor))}
Metade do preço: {formatarMoeda(metade(valor))}
{aumento}% de aumento: {formatarMoeda(aumentar(valor, aumento))}
{reducao}% de redução: {formatarMoeda(diminuir(valor, reducao))}''')