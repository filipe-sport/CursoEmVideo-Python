# DESAFIO 9 - Faça um programa que leia um número e mostrena tela a sua tabuada#
num9 = int(input("Digite um número para ver sua tabuada: "))
for i in range(10):
    i = i + 1
    print(f'{num9} x {i} = {num9*i}')