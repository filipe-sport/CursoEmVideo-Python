"""Crie um programa que leia o nome completo de uma pessoa e mostre:
   - Nome com todas as letras maiusculas
   - Nome com todas as letras minusculas
   - Quantas letras ao todo (sem contar com os espaços)
   - Quantas letras tem o primeiro nome
"""
nome = input("Entre com seu nome completo: ").strip()
print(nome.upper())
print(nome.lower())
"""print(len(nome)-nome.count(" "))""" 
print(len(nome.replace(" ","")))
print(len(nome.split()[0]))