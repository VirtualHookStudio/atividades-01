#12. GORJETA
#===========================================
#
#Enunciado: 
#Crie uma funcao que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de 
#gorjeta desejada.
#Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.â€‹
#
#â€‹ParÃ¢metros:â€‹
#
#- valor_conta (float): O valor total da contaâ€‹
#- porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)â€‹
#
#â€‹Retorna:â€‹
#O valor da gorjeta calculadaâ€‹â€‹

def gorjeta(v, g):
    gor = round(v * (g / 100))
    print(f"O valor da gorjeta e %{gor}")

valor = 0.0
porcentagem = 0.0

try:
    valor = round(float(input("Digite a conta: ")), 2)
except ValueError:
    print("Numero invalido")
    exit()

try:
    porcentagem = round(float(input("Digite a porcentagem: ")), 2)
except ValueError:
    print("Numero invalido")
    exit()

gorjeta(valor, porcentagem)