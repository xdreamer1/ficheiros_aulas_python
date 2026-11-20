class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("Som genérico")

class Cao(Animal):
    def __init__(self, nome, idade, raça):
        super().__init__(nome, idade)
        self.raça = raça

    def falar(self):
        print("Woof")

class gato(Animal):
    def __init__(self, nome, idade, raça):
        super().__init__(nome, idade)
        self.raça = raça
    
    def falar(self):
        print("Miau")

resposta = input("O teu animal é um cão ou gato?").strip().lower()

if resposta in ("cão", "cao"):

    meu_cao = Cao("Rex", 3, "Amigo")

    print(meu_cao.nome)

    print(meu_cao.idade)

    print(meu_cao.raça)

    meu_cao.falar()

elif resposta == "gato":
    
        meu_gato = gato("Cafe", 18, "Siames")

        print(meu_gato.nome)

        print(meu_gato.idade)

        print(meu_gato.raça)

        meu_gato.falar()

else: print("Animal não incluido.")