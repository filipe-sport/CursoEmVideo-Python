frase = "Curso em Video Python"
print(frase[9])
print(frase[9:13])
print(frase [9:21])
print(frase [9:21:2])
print(frase[:5])
print(frase[15:])
print(frase [9::3])

# Análise

print(len(frase))
print(frase.count("o",0,13))
print(frase.find("deo"))
print(frase.find("android"))
print("Curso" in frase)

# Transformação

print(frase.replace("Python", "Android"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase1 = "      Aprenda Python      "
print(frase1)
print(frase1.strip())
print(frase1.rstrip())
print(frase1.lstrip())

# Divisão

print(frase.split())
print(frase.split()[0])
print(frase.split()[0][0])


# Junção
print("-".join(frase))
