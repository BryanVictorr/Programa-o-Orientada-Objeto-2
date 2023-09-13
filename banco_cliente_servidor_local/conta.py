from historico import Historico

class Conta():

    def __init__(self, cliente):
        self._titular = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def cpf(self):
        return self._titular._cpf

    @property
    def historico(self):
        return self._historico

    def deposito(self, valor):

        if (valor > 0):
            self._saldo += valor
            self._historico._transacoes.append('Deposito de {}'.format(valor))
            return True
        else:
            return False

    def saque(self, valor):

        if (valor > 0):
            self._saldo -= valor
            self._historico._transacoes.append('Saque de {}'.format(valor))
            return True
        else:
            return False

    def transfere(self, destino, valor):

        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            destino._saldo += valor
            self._historico._transacoes.append('Transferencia enviada de {}'.format(valor))
            destino._historico._transacoes.append('Transferencia Recebida de {}'.format(valor))
            return True