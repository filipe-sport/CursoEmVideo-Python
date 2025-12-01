# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = input('Entre com seu nome completo: ')
pesquisa = nome.upper().split()
encontrado = nome.find('SILVA')

if pesquisa[encontrado] == 'SILVA':
    print('O nome digitado tem Silva')
else:
    print('O nome digitado não tem Silva')

