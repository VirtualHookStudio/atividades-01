#10. VERIFICADOR DE SENHAS
#===========================================
#
#- Crie um programa que verifique se uma senha e forte. 
#- Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um numero. 
#- O programa deve continuar pedindo senhas ate que uma senha valida seja inserida ou o usuario digite 'sair'.

while True:
    senha = str(input("Digite sua senha (minimo 8 caracteres): "))
    if len(senha) < 8:
        print("Senha invalida, necessario ao menos 8 caracteres")
        valor = str(input("Digite 'sair' caso queira sair da aplicacao: ")).lower()
        if valor == 'sair':
            break
    else:
        break