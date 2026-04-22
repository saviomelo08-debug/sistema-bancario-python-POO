from datetime import datetime

class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, operacao: str, valor: float):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self._transacoes.append(f"{data} - {operacao}: R$ {valor:.2f}")

    def listar_transacoes(self):
        if not self._transacoes:
            print("Nenhuma transação realizada.")
        for t in self._transacoes:
            print(t)