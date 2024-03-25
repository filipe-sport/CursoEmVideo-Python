#DESAFIO 8 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros#
metros = float(input("Digite distancia em metros: "))
print(f"A medida de {metros}m corresponde a:\n {metros/1000}km \n {metros/100}hm \n {metros/10} \n"
      f"{metros*10:.0f}dm \n {metros*100:.0f}cm \n {metros*1000:.0f}mm ")