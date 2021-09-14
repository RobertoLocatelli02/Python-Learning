def resultadoNotas(notas):
    resultado = {}
    resultado['totalNotas'] = len(notas)
    resultado['maiorNota'] = max(notas)
    resultado['menorNota'] = min(notas)
    resultado['media'] = sum(notas) / len(notas)
    return resultado

def pegaNotas():
    notas = []
    while True:
        totalNotas = int(input("Informe o total de notas a serem inseridas: "))
        if totalNotas > 0:
            break
        print("Quantidade de provas tem que ser maior que 0")
    i = 0
    while i < totalNotas:
        nota = float(input(f"Digite a {i + 1}º nota: "))
        notas.append(nota)
        i += 1
    return notas

def main():
    notas = pegaNotas()
    print(resultadoNotas(notas))

if __name__ == "__main__":
    main()