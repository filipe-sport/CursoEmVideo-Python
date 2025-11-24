# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.
import random
aluno1 = str(input('Entre com o nome do primeiro aluno: '))
aluno2 = str(input('Entre com o nome do segundo aluno: '))
aluno3 = str(input('Entre com o nome do terceiro aluno: '))
aluno4 = str(input('Entre com o nome do quarto aluno: '))

classe = [aluno1, aluno2, aluno3, aluno4]

print(f'O aluno escolhido para apagar o quadro foi: {random.choice(classe)}')