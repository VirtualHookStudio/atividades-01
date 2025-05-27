import requests

class Location:
    def __init__(self, logradouro, bairro, cidade, estado):
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"{self.logradouro} {self.bairro} {self.cidade} {self.estado}"

try:
    cep = int(input("Digite o CEP (Deve conter apenas numeros): "))
    API = requests.get(f"https://viacep.com.br/ws/{cep}/json")
    data = ""
    if API.status_code == 200:
        data = API.json()

        l = Location(
            logradouro = data["logradouro"],
            bairro = data["bairro"],
            estado = data["localidade"],
            cidade = data["uf"]
        )

        print("CEP consultado:")
        print(l.logradouro)
        print(l.bairro)
        print(l.estado)
        print(l.cidade)
    else:
        print("Nao foi possivel retornar valores!")

except ValueError:
    print("Numero do CEP invalido!")