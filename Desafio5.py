#DESAFIO 5 - Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor
num5 = int(input("Digite um número: "))
print(f"Analisando o valor {num5}, seu antecessor é {num5-1} e o sucessor é {num5+1}")

#DESAFIO 6 - Crie um algorithmo que leia um número e mostre o seu dobro, triplo e raiz quadrada#
num6 = int(input("Digite um número: "))
print(f" O dobro de {num6} vale {num6*2}.\n O triplo de {num6} vale {num6*3}.\n A raiz quadrada de {num6} vale {num6**2}")

#DESAFIO 7 -Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média#
nota1 = float(input("Primeira nota do aluno: "))
nota2 = float(input("Segunda nota do aluno: "))
media = ((nota1+nota2)/2)
print(f"A média entre {nota1} e {nota2} é igual a {media}")
#DESAFIO 8 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros#
metros = float(input("Digite distancia em metros: "))
print(f"A medida de {metros}m corresponde a:\n {metros/1000}km \n {metros/100}hm \n {metros/10} \n {metros*10:.0f}dm \n {metros*100:.0f}cm \n {metros*1000:.0f}mm ")
# DESAFIO 9 - Faça um programa que leia um número e mostrena tela a sua tabuada#
num9 = int(input("Digite um número para ver sua tabuada: "))
for i in range(10):
    i = i + 1
    print(f'{num9} x {i} = {num9*i}')

# DESAFIO 10 - Crie um programa que leia quanto dinheiro tenho na carteira e mostre quantos dólares ela pode comprar#
dinheiro = float(input("Quanto dinheiro você tem na sua carteira? R$"))
dolares = dinheiro * 5,16
print(f"Com R${dinheiro} você pode comprar U${dolares:.1f}")
#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pinta-la,cê 
#sabendo que cada litro de tinta pinta uma área de 2m²"""
#Faca um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.#
#Faça um algorítimo que leia o salário de um funcionario e mostre seu novo salario com 15% de aumento#




