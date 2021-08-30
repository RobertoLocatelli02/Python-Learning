"""
nome = input("Qual o seu nome?\n")
print("Olá," + nome + ", seja bem vindo ao programa\n\n")

dia = input("Informe a data de nascimento \nDia: ")
mes = input("Mês: ")
ano = input("Ano: ")
print(nome + " nasceu no dia " + dia + "/" + mes + "/" + ano + "\n\n")

numero1 = int(input("informe o primeiro número\n"))
numero2 = int(input("informe o segundo número\n"))
soma = numero1 + numero2
print("\nA soma vale:", soma)
print("A soma entre {} e {} vale {}".format(numero1, numero2, soma))

valor = input("Digite algo:")
print("esse valor é uma letra?", valor.isalpha())
print("esse valor é um número?", valor.isnumeric())
print("esse valor é alfa-numérico?", valor.isalnum())

numero = int(input("Informe um valor inteiro: "))
print(f"Antecessor = {numero-1} \nSucessor = {numero+1}")
numero = float(input("Informe um número:"))
print(f"O dobro desse número é {numero*2} \nO triplo é {numero*3} \nSua raíz quadrada é {numero**(1/2)}")

nota1 = float(input("Informe a primeira nota: \n"))
nota2 = float(input("Informe a segunda nota: \n"))
print(f"A média das notas {nota1} e {nota2} é igual a {(nota1+nota2)/2}")

print(20*"*", "\nConversor de medidas\n" + 20*"*")
metro = float(input("Insira um valor: \n"))
print(f"{metro} metros é igual à {metro*100} centimetros e {metro*1000} milímetros")

print(20*"*", "\nTabuada\n" + 20*"*")
num = int(input("insira um número: \n"))
print(f"{num} X 1 = {num*1}")
print(f"{num} X 2 = {num*2}")
print(f"{num} X 3 = {num*3}")
print(f"{num} X 4 = {num*4}")
print(f"{num} X 5 = {num*5}")
print(f"{num} X 6 = {num*6}")
print(f"{num} X 7 = {num*7}")
print(f"{num} X 8 = {num*8}")
print(f"{num} X 9 = {num*9}")
print(f"{num} X 10 = {num*10}")

print(19*"*", "\nConversor de moedas\n" + 19*"*")
valor = float(input("insira um valor:\n"))
print(f"US${valor} = R${valor*3.27}")

largura = float(input("Insira a largura:\n"))
altura = float(input("Insira a altura:\n"))
print(f"Em uma parede de {largura} metros por {altura} metros, serão necessários {(largura*altura)/2} litros de tinta para pintar tudo")

preco = float(input("Informe o valor de um produto:\n"))
print(f"Valor do produto R${preco}, com 5% de desconto passa a ser {preco-((5/100)*preco)}")

salario = float(input("Informe o salário:\n"))
print(f"Salário atual: R${salario} \nSalário com 15% de aumento: R${salario+((15/100)*salario)}")

import random
num = random.randint(1,10) #gera um numero inteiro aleatório entre 1 e 10
print(num)

import emoji
print(emoji.emojize("Olá, mundo :sunglasses:", use_aliases=True))

from math import trunc
numero = float(input("Digite um valor decimal: \n"))
print(f"Truncado com um integral: {numero.__trunc__}")

import math
cateto1 = float(input("Informe o cateto oposto:\n"))
cateto2 = float(input("Informe o cateto adjacente:\n"))
print(f"Hipotenusa terá {math.sqrt(math.pow(cateto1,2)+math.pow(cateto2,2))} de comprimento")

import math
angulo = int(input("Informe um ângulo:\n"))
print(f"Sen{angulo}° = {math.sin(angulo)} \nCos{angulo}° = {math.cos(angulo)} \nTg{angulo}° = {math.tan(angulo)}")

import random
nome1 = input("Insira o nome do primeiro aluno:\n")
nome2 = input("Insira o nome do segundo aluno:\n")
nome3 = input("Insira o nome do terceiro aluno:\n")
nome4 = input("Insira o nome do quarto aluno:\n")
nome = [nome1, nome2, nome3, nome4]
print(f"Quem vai apagar o quadro é {random.choice(nome)}")
nome = random.sample(nome, 4)
print("Ordem sorteada:\n",nome)

from math import trunc
numero = float(input("Digite um valor decimal: \n"))
print(f"Truncado com um integral: {numero.__trunc__()}")

from playsound import playsound
playsound("C:/Users/rloca/Music/olha-o-barulhinho.mp3")

frase = "Curso em video python"
frase = frase.replace(frase[0], "J")
print(frase)

nome = input("Informe seu nome completo:\n")
print(f"len {nome.__len__()}") #quantidade de caracteres
print(f"count {nome.count('o')}") #quantidade de caracteres especificados no parenteses
print(f"find {nome.find('domingos')}") #posição que começa um determinando nome
print(f"in {'locatelli' in nome}") #retorna true/false se a string especificada está em nome
print(f"replace {nome.replace('roberto', 'raphael')}") #troca uma string para outra string especificada
print(f"upper {nome.upper()}") #retorna nome com todas as letras maiusculas
print(f"lower {nome.lower()}") #retorna nome com todas as letras minusculas
print(f"capitalize {nome.capitalize()}") #retorna nome com apenas a primeira letra maiusucula
print(f"title {nome.title()}") #retorna nome com a primeira letra de cada nome em maiusculo
#print(f"strip {nome.strip()}")
#print(f"join {'-'.join(nome)}")

nome = input("Informe seu nome completo:\n")
print(f"Nome completo com todas as letras maiusculas: {nome.upper()}")
print(f"Nome completo com todas as letras minusculas: {nome.lower()}")
print(f"Quantidade de caracteres no nome: {nome.__len__() - nome.count(" ")}")
print(f"Quantidade de caracteres no primeiro nome: {nome.find(" ")}")

num = int(input("digite um valor entre 0 e 9999:\n"))
unidade = num % 10
dezena = int(((num - unidade) / 10) % 10)
centena = int((((num - unidade) - (dezena * 10)) / 100) % 10)
milhar = int(((num - unidade) - (dezena * 10) - (centena * 100)) / 1000)
print(f"unidade: {unidade} \ndezena: {dezena} \ncentena: {centena} \nmilhar: {milhar}")

cidade = input("Digite o nome da cidade:\n").strip().title()
print(cidade[:5] == "Santo")

nome = input("Digite seu nome completo:\n").title()
print(f" seu nome tem silva? {'Silva' in nome}")

nome = input("Digite seu nome completo:\n").lower().strip()
print(f"O nome tem {nome.count('a')} letras A \nO primeiro A aparece na posição {nome.find('a') + 1} \nO ultimo A aparece na posição {nome.rfind('a') + 1}")

nome = input("Digite seu nome completo:\n").title().strip()
nome = nome.split()
print(f"Seu primeiro nome é {nome[0]} \nSeu último nome é {nome[len(nome)-1]}")

nome = input("Qual o seu nome?\n").strip().title()
if nome == "Roberto":
    print("Você tem um nome lindo")
else:
    print("Você tem um nome tão normal")
print(f"Bom dia, {nome}!")

import random
numeroPensado = random.randint(0,5)
numeroInserido = int(input("Digite um número entre 0 e 5: "))
if numeroPensado == numeroInserido:
    print("Usuário venceu")
else:
    print("Usuário perdeu")

velocidade = float(input("Informe a velocidade do carro: "))
if velocidade <= 50:
    print("carro estava dentro da velocidade permitida")
else:
    excesso = velocidade - 50
    print(f"carro estava acima da velocidade permitida, valor da multa: R${excesso * 7}")

num = int(input("Informe um número: "))
if num % 2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")

distancia = float(input("Quantos quilômetros a viagem?\n"))
if distancia <= 200:
    preco = distancia * 0.50
    print(f"valor da viagem: {preco}")
else:
    preco = distancia * 0.45
    print(f"preço da viagem: {preco}")

ano = int(input("Informe o ano: "))
if ano % 4 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print(f"o menor valor é o {menor}")

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f"o maior valor é o {maior}")

salario = float(input("Informe o salário: R$"))
if salario <= 1250:
    salario += (salario * 0.15)
else:
    salario += (salario * 0.10)
print(f"Salário com o aumento: R${salario}")

reta1 = float(input(('Informe a primeira reta do triangulo: ')))
reta2 = float(input('Informe a segunda reta do triangulo: '))
reta3 = float(input('Informe a terceira reta do triângulo: '))
if reta1 > (abs(reta2 - reta3)) and reta1 < (reta2 + reta3):
    print(f"As retas {reta1}, {reta2} e {reta3} podem formar um triangulo")
elif reta2 > (abs(reta1 - reta3)) and reta2 < (reta1 + reta3):
    print(f"As retas {reta1}, {reta2} e {reta3} podem formar um triangulo")
elif reta3 > (abs(reta1 - reta2)) and reta3 < (reta1 + reta2):
    print(f"As retas {reta1}, {reta2} e {reta3} podem formar um triangulo")
else:
    print(f"As retas {reta1}, {reta2} e {reta3} não podem formar um triângulo")

import random
for i in range(7):
    num = random.randint(1,20)
    print(num)
"""

for i in range(10):
    print(i)