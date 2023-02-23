from ContaCorrente import ContaCorrente, CartaoCredito
import Agencia




conta_vitor = ContaCorrente('Vitor', '111.111', 111, 8090 )
cartao_vitor = ('Vitor', conta_vitor)


conta_vitor.depositar(100)


conta_vitor.consultar_saldo()
conta_vitor.consultar_historico_transacoes()