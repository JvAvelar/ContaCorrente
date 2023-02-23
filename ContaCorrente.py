from datetime import datetime
import pytz
from random import randint



class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario = datetime.now(fuso_br)
        return horario.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite_dever = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self._cartoes = []

    def consultar_saldo(self):
        print(f'Seu saldo atual é R${self._saldo:,.2f}')

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((f'Valor recebido: R${valor:,.2f}', f'Saldo da conta: {self._saldo:,.2f}',
                                f'Data da Transação: {ContaCorrente._data_hora()}'))

    def _limite_conta(self):
        self._limite_dever = -1000
        return self._limite_dever

    def sacar(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((f'Valor retirado: R${-valor:,.2f}', f'Saldo da conta: {self._saldo:,.2f}',
                                    f'Data da Transação: {ContaCorrente._data_hora()}'))

    def consultar_limite(self):
        print(f'O limite de cheque especial da sua conta é R${self._limite_conta():,.2f}')

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        if self._saldo - valor < 0:
            return 'Saldo insufiente'
        else:
            self._saldo -= valor
            self._transacoes.append((f'Valor retirado: R${-valor:,.2f}', f'Saldo da conta: {self._saldo:,.2f}',
                                    f'Data da Transação: {ContaCorrente._data_hora()}'))

            conta_destino._saldo += valor
            conta_destino._transacoes.append((f'Valor recebido: R${valor:,.2f}',
                                         f'Saldo da conta: {conta_destino._saldo:,.2f}',
                                         f'Data da Transação: {ContaCorrente._data_hora()}'))



class CartaoCredito():

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario = datetime.now(fuso_br)
        return horario

    def __init__(self, nome, conta_corrente):
        self._titular = nome
        self._numero =  randint(1000000000000000, 9999999999999999)
        self._validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year+4}'
        self._cvc = f'{randint(0,9)}{randint(0,9)}{randint(0,9)}'
        self._limite = 1000
        self._senha = '123456'
        self._conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)

    def aumento_limite(self, valor):
        self._limite += valor

    @property
    def senha(self):
        return self._senha


    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) == 6 and nova_senha.isnumeric():
            self._senha = nova_senha
        else:
            print('Senha inválida')