# Declaração da classe

class Gafanhoto:
    def __init__(self, n = 'vazio', i = 0): # Método construtor
        self.nome = n
        self.idade = i
    
    # Métodos de instância
    def aniversario(self):
        self.idade += 1 

    def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade.'


# Declaração dos objetos
g1 = Gafanhoto(input('Entre com seu nome: '), int(input('Entre com sua idade: ')))
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto(input('Entre com o segundo nome: ') , int(input("Entre com sua idade: ")) )
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())