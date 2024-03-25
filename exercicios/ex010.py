# DESAFIO 10 - Crie um programa que leia quanto dinheiro tenho na carteira e mostre quantos dólares ela pode comprar#
dinheiro = float(input("Quanto dinheiro você tem na sua carteira? R$"))
dolares = dinheiro * 5,16
print(f"Com R${dinheiro} você pode comprar U${dolares:.1f}")