import math
ang = float(input("Digite o angulo que voce deseja: "))
print(f"O ângulo de {ang} tem o seno  de {math.sin(math.radians(ang)):.2f}\n"
      f"O ângulo de {ang} tem o cosseno de {math.cos(math.radians(ang)):.2f}\n"
      f"O ângulo de {ang} tem a tangente de {math.tan(math.radians(ang)):.2f}" )
