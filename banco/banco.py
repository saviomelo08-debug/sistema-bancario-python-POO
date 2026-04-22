from contas.conta import Conta

class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

    def buscar_conta(self, numero: int) -> Conta:
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None