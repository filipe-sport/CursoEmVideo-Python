# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nomeCompleto = str(input("Entre com seu nome completo: "))

print(nomeCompleto.upper())
print(nomeCompleto.lower())
print(len(nomeCompleto.replace(' ','').strip()))
print(len(nomeCompleto.split()[0]))