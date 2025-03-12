class Conta_bancaria:
    taxa_juros = 0.05
    total_contas = 0

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        Conta_bancaria.total_contas += 1

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor inválido. O valor deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            if valor <= 0:
                print("Valor inválido. O valor do saque deve ser positivo.")
            else:
                print("Saldo insuficiente para o saque.")

    def verificar_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R${self.saldo}")

    @classmethod
    def ajustar_taxa_juros(cls, nova_taxa):
        if nova_taxa >= 0:
            cls.taxa_juros = nova_taxa
            print(f"Nova taxa de juros ajustada para: {cls.taxa_juros * 100}%")
        else:
            print("A taxa de juros deve ser positiva.")

    @classmethod
    def mostrar_total_contas(cls):
        print(f"Total de contas bancárias criadas: {cls.total_contas}")

    @staticmethod
    def converter_moeda(valor, taxa_conversao):
        return valor * taxa_conversao

    @staticmethod
    def dias_no_ano():
        return 365

conta1 = Conta_bancaria("Lucas", 500)
conta2 = Conta_bancaria("Maria", 300)

conta1.depositar(200)
conta2.depositar(-50)

conta1.sacar(100)
conta2.sacar(400) 

conta1.verificar_saldo()
conta2.verificar_saldo()

Conta_bancaria.ajustar_taxa_juros(0.03)

Conta_bancaria.mostrar_total_contas()

valor_convertido = Conta_bancaria.converter_moeda(100, 5.5)
print(f"Valor convertido: R${valor_convertido}")

dias = Conta_bancaria.dias_no_ano()
print(f"Número de dias no ano: {dias}")