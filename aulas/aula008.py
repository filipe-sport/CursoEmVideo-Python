"""import math
num = int(input("Digite um número: "))
raiz =math.sqrt(num)
print(f"A raiz de {num} é igual a {raiz:.2f}")
print("--------------------------------")
print(f"A raiz de {num} arredondada para cima é igual a {math.ceil(raiz)}")
print("--------------------------------")
print(f"A raiz de {num} arredondada para baixo é igual a {math.floor(raiz)}")"""

print(20*("--~~~"))

from math import sqrt, floor,ceil
num1 = int(input("Digite um número: "))
raiz =sqrt(num1)
print(f"A raiz de {num1} é igual a {raiz:.2f}")
print("--------------------------------")
print(f"A raiz de {num1} arredondada para cima é igual a {ceil(raiz)}")
print("--------------------------------")
print(f"A raiz de {num1} arredondada para baixo é igual a {floor(raiz)}")

print(20*("--~~~"))

import random
num2 = random.randint(1,10)
print(num2)


