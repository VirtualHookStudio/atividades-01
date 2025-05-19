#HELLO WORLD
print("Bem vindo ao programa.")

#SOMA DE DOIS NUMEROS
a = 1
b = 2

print("Resultado valor: ", a+b)

#CALCULO DO VOLUME DE UMA CAIXA RETANGULAR

a = 1
b = 2
c = 3

print("Resultado volume: ", a*b*c)

#TOTAL DA COMPRA
class Product:
    name = "Moto"
    price = 5.20
    quant = 2

print("Total valor: ", Product.price * Product.quant)

#CLASSIFICADOR DE IDADE
def printIdade(v):
    print(v)

idade = int(input("Digite a idade:"))

if idade >= 0 and idade <= 12:
    printIdade("Crianca")
elif idade >= 13 and idade <= 17:
    printIdade("Adolescente")
elif idade >= 18 and idade <= 59:
    printIdade("Adulto")
elif idade >= 60:
    printIdade("Idoso")
else:
    printIdade("Valor invalido")

#CALCULADORA DE IMC
def printIMC(v):
    print(v)

peso = round(float(input("Digite o peso: ")), 2)
altura = round(float(input("Digite a altura: ")), 2)

imc = round(peso / (altura ** 2), 2)

print("Seu IMC e de: ", imc)

if imc < 18.5:
    printIMC("Baixo peso")
elif imc >= 18.5 and imc <= 24.9:
    printIMC("Peso normal")
elif imc >= 25 and imc <= 29.9:
    printIMC("Excesso de peso")
elif imc >= 30 and imc <= 34.9:
    printIMC("Obesidade")
else:
    printIMC("Obesidade extrema")

#VERIFICADOR DE ANO BISSEXTO
ano = int(input("Digite o ano: "))

bissexto = False

if (ano * 4) == 0:
    bissexto = True
elif (ano * 100) == 0:
    if(ano * 400) == 0:
        bissexto = True

if bissexto:
    print("Ano Bissexto")
else:
    print("Ano nao Bissexto")