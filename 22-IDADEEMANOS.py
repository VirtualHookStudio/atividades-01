#14. IDADE EM ANOS
#===========================================
#
#Crie uma funcao que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def calculoDias(diaNascimento, mesNascimento, anoNascimento, anoAtual, mesAtual, diaAtual):
    count = 0

    # SOMA DOS DIAS DO ANO DE NACIMENTO
    for i in range(mesNascimento - 1, 12):
        if i == mesNascimento - 1:
            count += meses[i] - diaNascimento
        else:
            count += meses[i]
    if anoBissexto(anoNascimento) and mesNascimento <= 2:
        count += 1

    #SOMA DOS DIAS DOS ANOS COMPLETOS ENTRE NASCIMENT E ANO ATUAL
    for ano in range(anoNascimento + 1, anoAtual):
        count += 366 if anoBissexto(ano) else 365

    #SOMA OS DIAS DO ANO ATUAL
    for i in range(mesAtual - 1):
        count += meses[i]
    count += diaAtual
    if anoBissexto(anoAtual) and mesAtual > 2:
        count += 1

    print("Quantidade de dias que a pessoa tem: ", count)


    
    



def anoBissexto(a):
    return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)

try:
    dia = int(input("Informe o dia de seu nascimento: "))
    mes = int(input("Informe o mes de seu nascimento: "))
    ano = int(input("Informe o ano de seu nascimento: "))

    diaAtual = int(input("Informe o dia atual: "))
    mesAtual = int(input("Informe o mes atual: "))
    anoAtual = int(input("Informe o ano atual: "))

    calculoDias(dia, mes, ano, anoAtual, mesAtual, diaAtual)
except ValueError:
    print("Valor invalido!")