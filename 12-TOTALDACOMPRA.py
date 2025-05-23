#4. TOTAL DA COMPRA
#===========================================
#
#Objetivo:
#Calcular o valor total a ser pago por um determinado numero de unidades de um produto.
#
#Instrucoes:
#- Escreva um programa que armazene o nome de um produto, seu preco unitario e a quantidade comprada.
#- Calcule o valor total da compra e apresente uma descricao detalhada da transacao.
#
#Explicacao:
#- O valor total e obtido multiplicando o preco unitario pela quantidade comprada.
#- Alem do calculo, a clareza na apresentacao das informacoes e essencial para a compreensao do usuario.
#- O programa deve fornecer uma visao geral da compra, como se fosse um recibo simples.

class Product:
    name = "Moto"
    price = 5.20
    quant = 2

print("==== Detalhes da Compra ====")
print(f"Produto: ", Product.name)
print(f"Preço unitário: R$", Product.price)
print(f"Quantidade: ", Product.quant)
print("Total valor: ", Product.price * Product.quant)