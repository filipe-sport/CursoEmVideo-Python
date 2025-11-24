# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno1 = str(input('Entre com o nome do primeiro aluno: '))
aluno2 = str(input('Entre com o nome do segundo aluno: '))
aluno3 = str(input('Entre com o nome do terceiro aluno: '))
aluno4 = str(input('Entre com o nome do quarto aluno: '))

classe = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(classe)
print(f'A ordem de apresentação dos alunos é : {classe}')