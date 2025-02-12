# variavel global
x=10

class Exemplo:
    #variavel de classe (pode ser acessada por todas as instâncias da classe)
    y = 20
    def __init__(self):
        #Variável de instância (variavel local, pertence apenas a essa instancia)
        self.z = 30
    def acessar_variaveis(self):
        #varivel local (apenas desse metodo)
        w = 40
        print(f"Varivel global x: {x}")
        print(f"Varivel de classe y: {Exemplo.y}")
        print(f"Variavel de instância z: {self.z}")
        print(f"Variavel local w: {w}")
# Criando uma instacia da classe Exemplo
exemplo = Exemplo()
# Chamando o método acessar_variaveis
exemplo.acessar_variaveis()
# Acessando a variavel global fora da classe
print(f"\nAcessando a variavel global x fora da classe: {x}")