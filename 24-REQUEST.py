import requests
import json

class Person:
    def __init__(self, name, email, country):
        self.name = name
        self.email = email
        self.country = country

    def __str__(self):
        return f"{self.name} {self.email} {self.country}"
    
    

def personCreate():
    res = requests.get("https://randomuser.me/api/")
    data = res.json()
    person = data["results"][0]

    return Person(
        name = person["name"]["first"] + " " + person["name"]["last"],
        email = person["email"],
        country = person["location"]["country"]
    )

p = personCreate()

print("Pessoa gerada por API:")
print(p.name)
print(p.email)
print(p.country)