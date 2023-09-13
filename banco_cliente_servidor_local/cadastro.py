from tkinter.filedialog import SaveFileDialog
import mysql.connector
from cliente import Cliente

class Cadastro():

    __slots__ = ['_conexao','_cursor','_mysql']

    def __init__(self):
        self._conexao = mysql.connector.connect(host = 'localhost', user = 'bryanvictor', password = '32254632', database = 'bd2')
        self._cursor = self._conexao.cursor()
        self._mysql = """CREATE TABLE IF NOT EXISTS usuarios(nome varchar(30) NOT NULL,cpf varchar(11) PRIMARY KEY, nascimento varchar(10) NOT NULL, senha varchar(50) NOT NULL, saldo float NOT NULL, genero varchar(9) NOT NULL)"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()
        
        self._mysql = """CREATE TABLE IF NOT EXISTS historico(cpf varchar(11) PRIMARY KEY, historico varchar(10000))"""
        self._cursor.execute(self._mysql)
        self._conexao.commit()

    def cadastro(self, pessoa):
        verificar = self.busca(pessoa.cpf)

        if(verificar == None):
            self._cursor.execute('INSERT INTO usuarios(nome,cpf,nascimento,senha,saldo,genero) VALUES(%s,%s,%s,%s,%s,%s)',(pessoa.nome,pessoa.cpf,pessoa.nascimento,pessoa.senha,pessoa.saldo,pessoa.genero))
            self._conexao.commit()
            self._cursor.execute('INSERT INTO historico(cpf, historico) VALUES(%s,%s)',(pessoa.cpf, ""))
            self._conexao.commit()
            return True
        else:
            return False

    def busca(self, cpf):
        self._cursor.execute('SELECT * from usuarios WHERE cpf = %s',(cpf,))
        verificar = self._cursor.fetchone()
        
        if(verificar == None):
            return None
        else:
            pessoa = Cliente(verificar[0],verificar[1],verificar[2],verificar[3],float(verificar[4]),verificar[5])
            return pessoa

    def login(self, cpf, senha):

        verificar = self.busca(cpf)

        if(verificar.senha == senha):
            return verificar

        return None

    def deposito(self, cpf, valor):
        self._cursor.execute('UPDATE usuarios SET saldo = %s WHERE cpf = %s', (valor,cpf,))
        self._conexao.commit()

    def saque(self, cpf, valor):
        self._cursor.execute('UPDATE usuarios SET saldo = %s WHERE cpf = %s', (valor,cpf,))
        self._conexao.commit()


    def transfere(self, cpf, cpf_destino, valor_deposito, valor_saque):
        self._cursor.execute('UPDATE usuarios SET saldo = %s WHERE cpf = %s', (valor_saque,cpf,))
        self._cursor.execute('UPDATE usuarios SET saldo = %s WHERE cpf = %s', (valor_deposito,cpf_destino,))
        self._conexao.commit()

    def historico_deposito(self, cpf, valor):

        self._cursor.execute('SELECT * from historico WHERE cpf = %s',(cpf,))
        dados = self._cursor.fetchone()

        extrato = dados[1] + "Deposito realizado no valor de " + str(valor) + ","

        self._cursor.execute('UPDATE historico SET historico = %s WHERE cpf = %s', (extrato,cpf,))
        self._conexao.commit()

    def historico_saque(self, cpf, valor):

        self._cursor.execute('SELECT * from historico WHERE cpf = %s',(cpf,))
        dados = self._cursor.fetchone()

        extrato = dados[1] + "Saque realizado no valor de " + str(valor) + ","
        self._cursor.execute('UPDATE historico SET historico = %s WHERE cpf = %s', (extrato,cpf,))
        self._conexao.commit()

    def historico_transferencia(self, cpf_envio, cpf_destino, valor):

        self._cursor.execute('SELECT * from historico WHERE cpf = %s',(cpf_envio,))
        dados = self._cursor.fetchone()

        extrato_envio = dados[1] + "Transferencia enviada no valor de " + str(valor) + ","
        self._cursor.execute('UPDATE historico SET historico = %s WHERE cpf = %s', (extrato_envio,cpf_envio,))
        self._conexao.commit()

        self._cursor.execute('SELECT * from historico WHERE cpf = %s',(cpf_destino,))
        dados = self._cursor.fetchone()

        extrato_destino = dados[1] + "Transfrencia recebida no valor de " + str(valor) + ","
        self._cursor.execute('UPDATE historico SET historico = %s WHERE cpf = %s', (extrato_destino,cpf_destino,))
        self._conexao.commit()

    def historico(self, cpf):

        self._cursor.execute('SELECT * from historico WHERE cpf = %s',(cpf,))
        dados = self._cursor.fetchone()
        historico = dados[1]
        return historico