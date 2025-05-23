#14. IDADE EM ANOS
#===========================================
#
#Crie uma funcao que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def calculoDias(dia_nascimento, mes_nascimento, ano_nascimento, ano_atual, mes_atual, dia_atual):
    count = 0

    # SOMA DOS DIAS DO ANO DE NACIMENTO
    for i in range(mes_nascimento - 1, 12):
        if i == mes_nascimento - 1:
            count += meses[i] - dia_nascimento
        else:
            count += meses[i]
    if anoBissexto(ano_nascimento) and mes_nascimento <= 2:
        count += 1

    #SOMA DOS DIAS DOS ANOS COMPLETOS ENTRE NASCIMENT E ANO ATUAL
    for ano in range(ano_nascimento + 1, ano_atual):
        count += 366 if anoBissexto(ano) else 365

    #SOMA OS DIAS DO ANO ATUAL
    for i in range(mes_atual - 1):
        count += meses[i]
    count += diaAtual
    if anoBissexto(ano_atual) and mes_atual > 2:
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