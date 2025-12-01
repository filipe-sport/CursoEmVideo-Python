# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos dos digitos separados (unidade, dezena, centena e milhar)
numero = int(input('Entre com um numero entre 0 e 9999: '))

milhar = numero // 1000
centena = (numero-(milhar*1000)) // 100
dezena = (numero-(milhar*1000)-(centena*100)) // 10
unidade = (numero-(milhar*1000)-(centena*100)-(dezena*10))
print(f'O numero digitado tem:\n{milhar} milhar\n{centena} centena\n{dezena} dezena\n{unidade} unidade')