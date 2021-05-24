letra = str(input("Informe uma letra do alfabeto: ")).strip().lower()
if letra[0].isalpha():
    if letra[0] == "a" or letra[0] == "e" or letra[0] == "i" or letra[0] == "o" or letra[0] == "u":
        print("Sua letra é uma vogal")
    else:
        print("Sua letra é uma consoante")
else:
    print("Valor informado não corresponde à uma letra")