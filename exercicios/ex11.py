# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta, pinta uma área de 2m²

alt = float(input('Entre com a altura da parede: '))
larg = float (input('Entre com a largura da parede: '))

area = alt * larg

qtdTinta = area / 2

print(f'A quantidade de tinta para a pintar a parede de {area}m² é de {qtdTinta} litros. ')