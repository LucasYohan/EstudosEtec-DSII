class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def exibird_dados(self):
        return f'Nome: {self.nome}, Salário: {self.salario}'
    
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
        
    def exibird_dados(self):
        return f'Nome: {self.nome}, Salário: {self.salario} e Bônus: {self.bonus}'
        
        
class Programador(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem
        
    def exibird_dados(self):
        return f'Nome: {self.nome}, Salário: {self.salario} e Linguagem: {self.linguagem}'
    
    
    
Lucas = Funcionario('Lucas', 2000)
print(Lucas.exibird_dados())

Yohan = Gerente('Yohan', 5000, 1000)
print(Yohan.exibird_dados())

Leticia = Programador('Leticia', 3000, 'Python')
print(Leticia.exibird_dados())