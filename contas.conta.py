from clientes.cliente import Cliente
from operacoes.historico import Historico

class Conta:
    def __init__(self, numero: int, cliente: Cliente):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0.0 # Encapsulamento
        self.historico = Historico() # Composição

    @property
    def saldo(self(self):
        return self.__saldo

    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor
            self.historico.adicionar_transacao("Depósito", valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor: float) -> bool:
        pass # Será implementado nas subclasses (Polimorfismo)

    def _atualizar_saldo(self, valor: float):
        # Método interno para as subclasses modificarem o saldo de forma segura
        self.__saldo -= valor