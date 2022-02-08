from entity.Orcamento import Orcamento
# from entity.Time import Time
class Orcamento():
    def opcoes(self):
        print("Digite a opcão desejada: ")
        print("[1] Receita total")
        print("[2] saldo disponível")
        print("[3] Gastos")
        print("[4] Adicionar receita")
        print("[5] Adicionar dispensa")

        return input()
    
    def ver_gastos(self, time):
        print("Total gasto: ")