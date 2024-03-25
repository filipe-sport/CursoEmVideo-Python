"""Escreva um programa que a quantidade de KM percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo 
que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodados."""

diasAlugados = int(input("Quantos dias alugados: "))
kmRodados = float(input("Quantos KM rodados: ").replace(",", "."))
totalPago = (diasAlugados*60)+(kmRodados*0.15)
print(f"O total a pagar é {totalPago}")