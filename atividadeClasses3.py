# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome #Atributo de instancia
#         self.idade = idade

#     def Aniversario(self):
#         self.idade += 1

#     def cumprimentar (self):
#         print(f"Olá, meu nome é {self.nome}, e eu tenhos {self.idade} anos")



# pessoa = Pessoa("Maria", 30)
# pessoa.Aniversario()
# pessoa.cumprimentar()


class Pessoa:
    populacao = 0
    def __init__(self, nome):
        self.nome = nome
        Pessoa.populacao += 1

    @classmethod
    def mostrar_populacao(cls):
        print(f"A população atual é {cls.populacao}")

pessoa1 = Pessoa("Maria")
pessoa2 = Pessoa("João")
Pessoa.mostrar_populacao()