from math import hypot
catOpost = float(input("Comprimento do cateto oposto: "))
catAdjasc = float(input("Comprimento do cateto adjascente: "))
hipo = hypot(catOpost, catAdjasc)
print(f"A hipotenusa vai medir {hipo:.2f}")