class Cao:
    def __init__(self, nome, idade, raça):
        self.nome = nome
        self.idade = idade
        self.raça = raça

    def falar(self):
        print("Woof")

meu_cao = Cao("Rex", 3, "Amigo")

print(meu_cao.nome)

print(meu_cao.idade)

print(meu_cao.raça)

meu_cao.falar()