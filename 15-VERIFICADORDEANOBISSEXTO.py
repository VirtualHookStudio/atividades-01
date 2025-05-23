#7. VERIFICADOR DE ANO BISSEXTO
#===========================================
#
#Enunciado:
#Faca um programa que determine se um ano inserido pelo usuario e bissexto ou nao.
#Lembre-se:
#- Um ano e bissexto se for divisivel por 4;
#- Mas anos divisiveis por 100 so sao bissextos se tambem forem divisiveis por 400.
#
#Instrucoes:
#- Solicite que o usuario digite um ano.
#- Verifique se ele e bissexto ou nao, de acordo com as regras descritas.
#- Exiba uma mensagem informando se o ano e bissexto.
#
#Explicacao:
#- Este exercicio explora o uso de operadores logicos e condicionais compostos.
#- Trata-se de uma aplicacao classica que ajuda a desenvolver o raciocinio para multiplas condicoes encadeadas.
#- Teste com diferentes anos para validar a logica.

while True:
    try:
        ano = int(input("Digite o ano: "))
        break
    except ValueError:
        print("Valor invalido!")

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