#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
angulo = float(input('Entre com um ângulo: '))

print(f'Seno de {angulo} é: {(math.sin(math.radians(angulo))):.2} \nCosseno de {angulo} é: {math.cos(math.radians(angulo)):.2} \nTangente do angulo é: {math.tan(math.radians(angulo)):.2}')