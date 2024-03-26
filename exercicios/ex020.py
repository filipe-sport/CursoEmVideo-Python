import random
n1 = input("Entre com o primeiro aluno: ")
n2 = input("Entre com o segundo aluno: ")
n3 = input("Entre com o terceiro aluno: ")
n4 = input("Entre com o quarto aluno: ")
lista = [n1, n2, n3, n4]
random.shuffle(lista) # shuffle embaralhar a lista
print(f"A ordem de apresentação será: {lista} ")