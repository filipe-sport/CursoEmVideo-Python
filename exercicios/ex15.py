# Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 0.15 por Km rodado.

km = float(input('Entre com a quantidade de km percorrido: '))
dias = int(input('Entre com a quantidade de dias que o carro ficou alugado: '))

total = (km * 0.15) + (dias * 60)

print(f'Logo o total a ser pago pelo carro alugado é de : {total} ')