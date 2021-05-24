sexo = str(input("Informe o sexo: ")).strip().title()
if sexo[0] == "M":
    print("sexo informado: Masculino")
elif sexo[0] == "F":
    print("sexo informado: Feminino")
else:
    print("sexo inválido")
