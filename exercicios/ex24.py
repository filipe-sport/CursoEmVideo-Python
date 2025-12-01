# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
nomeCidade = input('Entre com o nome da cidade: ')
pesquisa = nomeCidade.upper().split()

if pesquisa[0] == 'SANTO':
    print('O nome da cidade começa com a palavra Santo')
else:
    print('O nome da cidade não começa com a palvra Santo')
