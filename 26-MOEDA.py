import requests

class Coin:
    def __init__(self, value_max, value_min, time):
        self.value_max = value_max
        self.value_min = value_min
        self.time = time

    def __str__(self):
        return f"{self.value_max} {self.value_min} {self.time}"

try:
    res = str(input("Digite a moeda desejada para comparar com o real: "))
    API = requests.get(f"https://economia.awesomeapi.com.br/json/last/{res}-BRL")
    
    data = ""
    if API.status_code == 200:
        data = API.json()
        
        c = Coin(
            value_max = data['USDBRL']["high"],
            value_min = data['USDBRL']["low"],
            time = data['USDBRL']["create_date"],
        )

        print("Moeda consultada:")
        print("Cotacao autal maxima: ", c.value_max)
        print("Cotacao autal maxima: ", c.value_min)
        print("Atualizado: ", c.time)
    else:
        print("Nao foi possivel retornar valores!")

except ValueError:
    print("Valor invalido!")