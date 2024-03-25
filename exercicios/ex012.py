# DESAFIO 12 - Faca um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.#
preco = float(input("Qual o preço do produto? R$ "))
novopreco = preco*0.95
print(f"O produto que custava {preco}, na promoção com desconto de 5% vai custar R$ {novopreco}")