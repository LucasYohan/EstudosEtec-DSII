class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(f"{self.nome} está latindo!")
        int(f"{self.idade} está latindo!")


#Criando um objeto da classe Cachorro

meu_cachorro = Cachorro("Rex", 2)
print(meu_cachorro.nome)
meu_cachorro.latir()