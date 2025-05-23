#13. PALINDROMO
#===========================================
#
#Crie uma funcao que verifique se uma palavra ou frase e um palindromo 
#(le-se igual de tras para frente, ignorando espacos e pontuacao). 
#Se o resultado E True, responda â€œSimâ€, se o resultado for False, responda â€œNao"
#

def palidromo(f):
    fraseInvertida = ""
    for v in reversed(f):
        fraseInvertida += v
    if(f == fraseInvertida):
        print("Palavra Palindromo")
    else:
        print("Palavra nao Palindromo")

fraseFiltrada = ""
frase = str(input("Digite uma palavra: ")).lower()
for caractere in frase:
    if caractere.isalpha():
        fraseFiltrada += caractere

palidromo(fraseFiltrada)

