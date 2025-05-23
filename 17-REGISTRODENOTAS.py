#9. REGISTRO DE NOTAS
#===========================================
#
#- Crie um programa que permita a um professor registrar as notas de uma turma. 
#- O programa deve continuar solicitando notas ate que o professor digite 'fim'. 
#- Notas vÃ¡lidas sÃ£o de 0 a 10. 
#- O programa deve ignorar notas invalidas e continuar solicitando. 
#- No final, deve exibir a mÃ©dia da turma. Notas = [] -> len(Notas)â€‹

notas = []

while True:
    try:
        valor = round(float(input("Digite a nota: ")), 1)
        notas.append(valor)
    except ValueError:
        print("Valor invalido!")
    
    add = "S"

    while True:
        try:
            add = str(input("Deseja adicionar mais notas? [S]-sim [N]-nao: ")).upper()
            if(add != "S" and add != "N"):
                print("Valor invalido")
            else:
                break
        except ValueError:
            print("Valor invalido")
    
    if add == "N":
        break

soma = 0

print("=========")
print("  Notas  ")
print("=========")

for nota in notas:
    print(nota)
    soma += nota

print("Total de notas: ", len(notas))
print("Media: ", round(soma / len(notas), 2))
