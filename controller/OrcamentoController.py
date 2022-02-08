import entity.Orcamento
import view.OrcamentoView
class OrcamentoController():

    def adiciona_receita(self, valor):
        entity.Orcamento.Orcamento.adiciona_receita(valor)
    
    def subtrai_receita(self, valor):
        entity.Orcamento.Orcamento.subtrai_receita(valor)
    
    def ver_saldo(self):
        view.OrcamentoView.Orcamento.ver_gastos()