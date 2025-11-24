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
print(frase.capitalize()) #só a primeira letra em maiuscula
print(frase.title())


