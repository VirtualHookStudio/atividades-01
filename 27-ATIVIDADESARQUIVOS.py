#O SCRIPT PODE LER E ESCREVER EM ARQUIVOS.TXT .CSV E .JSON (OS ARQUIVOS SAO SALVOS NA PASTA DATAS
#O SCRIPT SOLUCIONA AS 3 ATIVIDADES (2, 3, 4) DO DIA 28/05/20225
import csv
import json

choice = ""
archive = ""

information = ""

while choice == "":
    choice = str(input("Digite leitura[L] e escrita[E]: ")).upper()
    if choice == "L":
        choice = "r"
    elif choice == "E":
        write = str(input("Digite para salvar (todos separados por virgula): "))
        information = write.split(",")
        choice = "w"
    else:
        choice = ""
        print("Valor invalido!")

while archive == "":
    archive = str(input("Digite a extensao .txt | .csv | json: "))
    if  not archive  in [".txt", ".csv", ".json"]:
        archive = ""
        print("Valor invealido!")


with open(f"./datas/data{archive}", choice, encoding="utf8") as archive_data:
    if archive == ".txt":
        if choice == "r":
            content = archive_data.read()
            print(content)
        else:
            string = information[0] + "," + information[1] + "," + information[2]
            archive_data.write(string)
    if archive == ".csv":
        if choice == "r":
            content = csv.reader(archive_data)
            for line in content:
                print(line)
        else:
            content = csv.writer(archive_data)
            content.writerow(information)
    if archive == ".json":
        if choice == "r":
            content = json.load(archive_data)
            print(content)
        else:
            json.dump({"Nome": information[0], "Idade": information[1], "Cidade": information[2]}, archive_data, indent=4)