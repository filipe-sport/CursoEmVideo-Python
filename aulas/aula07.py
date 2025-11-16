print(5-2)
print(5+2)
print(5*2)
print(5/2)
print(5**2)
print(5//2) # divisão inteira
print(5%2) # resto da divisão

#Ordem de Precedência

# 1 () > Parenteses
# 2 ** > Exponeciação
# 3 * / // % > Multiplicação , Divisão, Divisão Inteira, Resto da Divisão
# 4 - + > Subtração, Soma

print(5 + 3 * 2)
print(5 ** 2)
print(5 ** 3)
print(19 / 2)
print(18 % 2)
print(122 % 3)
print(4 ** 3)
print(pow(4,3))
print(81 ** (1/2))
print(25 ** (1/2))
print(127 ** (1/3))
print('Oi' + 'Olá')
print('Oi' * 5)
print('=' * 20)


nome = input('Qual é seu nome? ')
print(f'Prazer em te conhecer {nome:20}!')
print(f'Prazer em te conhecer {nome:<20}!')
print(f'Prazer em te conhecer {nome:>20}!')
print(f'Prazer em te conhecer {nome:^20}!')
print(f'Prazer em te conhecer {nome:=^20}!')

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
s = num1 + num2
p = num1 * num2
d = num1 / num2
di = num1 // num2
e = num1 ** num2

print(f'A soma é {s}, o produto é {p}, a divisão é {d}', end=' ')
print(f'A divisão inteira é {di} e a potência é {e} ')