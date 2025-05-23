#6. CALCULADORA DE IMC
#===========================================
#
#Enunciado:
#Desenvolva um programa que calcule o Indice de Massa Corporal (IMC) de uma pessoa.
#O programa deve solicitar o peso (em kg) e a altura (em metros), calcular o IMC e informar a classificacao de acordo com a tabela padrao.
#
#Instrucoes:
#- Solicite os dados do usuario: peso e altura.
#- Calcule o IMC usando a formula: IMC = peso / (altura ** 2).
#- Exiba o valor do IMC com uma casa decimal e a respectiva classificacao (ex: abaixo do peso, normal, sobrepeso etc.).
#
#Explicacao:
#- O exercicio envolve entrada de dados numericos com ponto flutuante, calculos matematicos e estruturas condicionais.
#- A classificacao deve seguir os intervalos padrao definidos para o IMC.
#- Apresente o resultado de forma clara e arredondado corretamente.

while True:
    try:
        while True:
            peso = round(float(input("Digite o peso: ")), 2)
            if peso < 0:
                print("Valor invalido!")
            break

        while True:
            altura = round(float(input("Digite a altura: ")), 2)
            if altura < 0:
                print("Valor invalido!")
            break
        
        break
    except ValueError:
        print("Valor invalido!")

imc = round(peso / (altura ** 2), 2)

print("Seu IMC e de: ", imc)

if imc < 18.5:
    print("Baixo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Excesso de peso")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade")
else:
    print("Obesidade extrema")