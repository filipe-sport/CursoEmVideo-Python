# Declaração da classe

class Gafanhoto:
    def __init__(self): # Método construtor
        self.nome = ''
        self.idade = 0
    
    # Métodos de instância
    def aniversario(self):
        self.idade += 1 

    def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade.'


# Declaração dos objetos
g1 = Gafanhoto()
g1.nome = input("Entre com seu nome: ")
g1.idade = int(input("Entre com sua idade: "))
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = input('Entre com o segundo nome: ')
g2.idade = int(input("Entre com sua idade: "))
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())