from random import randint


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
        self.transacoes = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'O valor em caixa está abaixo do indicado. Valor atual R${self.caixa:,}')
        else:
            print(f'O valor em caixa está OK. Valor atual R${self.caixa:,}')

    def abastecer_caixa(self, valor):
        self.caixa += valor
        print('Depósito realizado com sucesso')

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.caixa -= valor
            self.emprestimos.append((valor, cpf, juros))
            print('Empréstimo em processamento')
        else:
            print('Empréstimo não disponível')

    def verificar_emprestimos(self):
        return self.emprestimos

    def adicionar_clientes(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))
        print('Cliente cadastrado com sucesso')

    def verificar_lista_clientes(self):
        print (self.clientes)



class AgenciaVirtual(Agencia):
    #usando super para herdar o init da classe principal
    #Junto com os demais atributos
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        if self.caixa >= valor:
            self.caixa -= valor
            self.caixa_paypal += valor
            print('Depósito realizado')
        else:
            print('Saldo insuficiente')

    def sacar_paypal(self, valor):
        if self.caixa_paypal >= valor:
            self.caixa_paypal -= valor
            self.caixa += valor
            print('Depósito realizado')
        else:
            print('Saldo insuficiente')

class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):

        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):

        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000
        self.clientes = []

    def adicionar_clientes(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_clientes(nome, cpf, patrimonio)
            print('Você agora é um novo cliente na Agência Premium')
        else:
            print('Você não possui patrimônio suficiente para entrar na Agência Premium')

if __name__ == '__main__':
    # programa test
    agencia1 = Agencia(1283931, 40000, 40)

    agencia_virtual = AgenciaVirtual(36251052, 102030, 4004)
    agencia_comum = AgenciaComum(2133243, 12312443)
    agencia_premium = AgenciaPremium(133834, 38934)

    agencia_virtual.adicionar_clientes('manu', 129910, 1000)
    agencia_premium.adicionar_clientes('vitor', 10920, 1100000)
    agencia_comum.adicionar_clientes('laura', 109290, 3000)

    agencia_premium.verificar_lista_clientes()
    agencia_virtual.verificar_lista_clientes()
    agencia_comum.verificar_lista_clientes()