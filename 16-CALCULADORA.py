#8. CALCULADORA
#===========================================
#Desenvolva uma calculadora em Python que realize as quatro operacoes basicas entre dois numeros. 
#A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operacao. Siga as especificacoes abaixo:â€‹
#
#- A calculadora deve solicitar ao usuario que insira dois numeros e uma operacao.â€‹
#- As operacoes validas sao: + (adicao), - (subtracao), * (multiplicacao) e / (divisao).â€‹
#- O programa deve continuar solicitando entradas ate que uma operacao valida seja concluida.â€‹
#
#Trate os seguintes erros:â€‹
#
#- Entrada invalida (nÃ£o numerica) para os numerosâ€‹
#- Divisao por zeroâ€‹
#- Operacao invalidaâ€‹
#
#- Use try/except para capturar e tratar os erros apropriadamente.â€‹
#- Apos cada erro, o programa deve informar o usuario sobre o erro e solicitar nova entrada.â€‹
#- Quando uma operacao e concluida com sucesso, exiba o resultado e encerre o programa.â€‹

while True:
    try:
        a = float(input("Digite o primeiro numero: "))
        b = float(input("Digite o segundo numero: "))
        break
    except ValueError:
        print("Valor invalido!")

operation = ""
resultado = 0

while operation != "*" and operation != "-" and operation != "+" and operation != "+" and operation != "/":
    while True:
        try:
            operation = str(input("Digite uma das operacoes [* (multiplicacao), - (subtracao), + (soma), / (divisao)]"))
            match operation:
                case "*":
                    resultado = a * b
                case "/":
                    resultado = a / b
                case "-":
                    resultado = a - b
                case "+":
                    resultado = a + b
                case _:
                    print("Operacao invalida, tente novamente!")
            break
        except ZeroDivisionError:
            print("Valor invalido: erro de divizao por zero")

print("Resultado: ", round(float(resultado), 5))