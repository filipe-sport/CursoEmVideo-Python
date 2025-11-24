# Faça um programa que leia o comprimento do cateto ooposto e do cateto adjacente de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa

cat1 = float(input('Entre com o valor do cateto: '))
cat2 = float(input('Entre com o valor do outro cateto: '))

hipot = ((cat1**2) + (cat2**2))**0.5

print(hipot)