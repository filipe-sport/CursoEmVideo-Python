"""Crie um programa que leia o nome completo de uma pessoa e mostre:
   - Nome com todas as letras maiusculas
   - Nome com todas as letras minusculas
   - Quantas letras ao todo (sem contar com os espaços)
   - Quantas letras tem o primeiro nome
"""
nome = input("Digite seu nome completo: ").strip()
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome)-nome.count(' ')} letras")
print(f"Seu primeiro nome tem {len(nome.split()[0])} letras")