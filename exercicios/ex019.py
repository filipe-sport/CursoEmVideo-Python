import random
n1 = input("Nome primeiro aluno: ")
n2 = input("Nome segundo aluno: ")
n3 = input("Nome terceiro aluno: ")
n4 = input("Nome quarto aluno: ")
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista) # choice escolhe um item aleatorio da lista
print(f"O aluno escolhido foi {escolhido}")
