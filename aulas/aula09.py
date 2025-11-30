frase = 'Curso em Video Python'

print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#Análise
print(len(frase)) # comprimento
print(frase.count('o')) #contagem
print(frase.count('o', 0, 13)) #contagem já com fatiamento
print(frase.find('deo')) #achar a posição de uma string
print('Curso' in frase) #cerificar se tem a string dentro de uma cadeia de caracteres
print(frase.replace('Python', 'Android')) #substitui na exibição uma palavra pela outra
print(frase.upper()) #tudo em maiusculo
print(frase.lower()) #tudo em minusculo
print(frase.capitalize()) #só a primeira letra da string em maiúscula
print(frase.title()) #a primeira letra de cada palavra em maiúscula

frase ='    Aprenda Python  '
print(frase.strip()) #elimina espaços em branco tanto no começo como no final da string
print(frase.rstrip()) #elimina espaços a direita da string
print(frase.lstrip()) #elimina espaços a esquerda da string
print(frase.split()) #divisão da string considerando os espaços
print(frase.split("y")) #divisão da string considerando os espaços, caso ("y") ele deliyitaria a partir da letra y





