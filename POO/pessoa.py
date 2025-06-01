class Pessoa():
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def dadosCompletos(self):
        print(f"Nome: {self.nome}, idade: {self.idade}, cidade: {self.cidade}")