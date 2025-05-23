#5. CLASSIFICADOR DE IDADE
#===========================================
#
#Enunciado:
#Crie um programa que solicite a idade do usuario e classifique-o em uma das seguintes categorias:
#- Crianca (0 a 12 anos)
#- Adolescente (13 a 17 anos)
#- Adulto (18 a 59 anos)
#- Idoso (60 anos ou mais)
#
#Instrucoes:
#- Solicite que o usuario digite sua idade.
#- O programa deve interpretar o valor digitado e classifica-lo de acordo com as faixas etÃ¡rias.
#- O resultado da classificacao deve ser exibido de forma clara.
#
#Explicacao:
#- Esse exercicio utiliza estruturas condicionais para tomar decisoes baseadas em faixas numericas.
#- Importante tratar casos invalidos, como idades negativas.
#- A logica deve garantir que nenhuma faixa se sobreponha ou fique sem cobertura.

while True:
    try:
        idade = int(input("Digite a idade:"))
        if(idade < 0):
            print("Valor invalido!")
        else:
            break
    except ValueError:
        print("Digite um valor valido!")

if idade >= 0 and idade <= 12:
    print("Crianca")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")