#11. PAR OU IMPAR
#===========================================
#
#Crie um programa que solicite ao usuario que insira numeros inteiros. 
#O programa deve continuar solicitando numeros ate que o usuario digite 'fim'. 
#Para cada numero inserido, o programa deve informar se e par ou impar. 
#Se o usuario inserir algo que nao seja um numero inteiro, o programa deve informar o erro e continuar. 
#No final, o programa deve exibir a quantidade de numeros pares e impares inseridos.

pares_count = 0
impares_count = 0

while True:
    try:
        valor = int(input("Digite um valor (necessario valor inteiro): "))
        if valor% 2 == 0:
            pares_count += 1
            print("Valor par")
        else:
            impares_count +=1
            print("Valor impar")
        print("======================================")
    except ValueError:
        print("Valor inteiro invalido!")
    
    sair = input("Digite 'fim' para sair da aplicacao: ")
    if isinstance(sair, str):
        if sair.lower() == "sair":
            break


print("Quantidade de numeros pares: ", pares_count)
print("Quantidade de numeros impares: ", impares_count)