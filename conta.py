class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Criando um objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo de {} é de {} reais".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print (f"O valor {valor} passou do limite")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def titular(self):
        return self.__titular

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return ("001")

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
