class Cliente():

    __slots__ = ['_nome','_cpf','_nascimento','_senha','_saldo','_genero']

    def __init__(self,nome, cpf, nascimento, senha, saldo , genero):
        self._nome = nome
        self._cpf = cpf
        self._senha = senha
        self._nascimento = nascimento
        self._saldo = saldo
        self._genero = genero

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def senha(self):
        return self._senha

    @property
    def nascimento(self):
        return self._nascimento

    @property
    def saldo(self):
        return self._saldo

    @property
    def genero(self):
        return self._genero

    @property
    def historico(self):
        return self._historico

    def deposito(self,valor):
        self._saldo += valor    
        return self._saldo

    def saque(self, valor):

        if(valor <= self._saldo):
            self._saldo -= valor
            return self._saldo
        else:
            return False

    def transfere(self, destino, valor):

        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            destino._saldo += valor
            return self._saldo, destino._saldo

