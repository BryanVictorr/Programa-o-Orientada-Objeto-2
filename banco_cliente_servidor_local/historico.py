class Historico:

    __slots__ = ['_transacoes']

    def __init__(self):
        self._transacoes = []

    def imprime(self):

        lista = ",".join(self._transacoes)
        lista = lista.replace(",","\n")
        return lista