#13. PALINDROMO
#===========================================
#
#Crie uma funcao que verifique se uma palavra ou frase e um palindromo 
#(le-se igual de tras para frente, ignorando espacos e pontuacao). 
#Se o resultado E True, responda â€œSimâ€, se o resultado for False, responda â€œNao"
#

def palidromo(f):
    frase_invertida = ""
    for v in reversed(f):
        frase_invertida += v
    if(f == frase_invertida):
        print("Palavra Palindromo")
    else:
        print("Palavra nao Palindromo")

frase_filtrada = ""
frase = str(input("Digite uma palavra: ")).lower()
for caractere in frase:
    if caractere.isalpha():
        frase_filtrada += caractere

palidromo(frase_filtrada)

