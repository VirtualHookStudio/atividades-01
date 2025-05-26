import random
import string

caractere = string.ascii_letters + string.digits + string.punctuation

try:
    quant = int(input("Informe a quantidade de caracteres da senha: "))
    if quant <= 0:
        raise Exception("O valor deve ser maior que zero!")

    ramdom = ''.join([random.choice(caractere) for n in range(quant)])

    print("Sua senha: ", ramdom)
except ValueError:
    print("Valor invalido!")
except Exception as e:
    print(e)