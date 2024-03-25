# DESAFIO 11 - Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pinta-la,
#sabendo que cada litro de tinta pinta uma área de 2m²
larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg * alt
print(f"Sua parede tem a dimensão de {larg} x {alt} e sua área é de {area:.2f}m².\n"
      f"Para pintar essa parede, você precisará de {(area/2):.0f}L de tinta")