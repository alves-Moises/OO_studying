

class Orcamento():
    def __init__(self, valor):
        self.__receitas = float()
        self.__despesas: float()
        self.__saldo = float()  # diferenca entre receita dispesas
    
    @property
    def receitas(self):
        return self.__receitas

    @property
    def despesas(self):
        return self.__despesas

    @property
    def saldo(self):
        return self.__saldo

    @receitas.setter
    def receitas(self, valor):
        self.__receitas = valor
        self.__saldo = self.__receitas - self.despesas


    @despesas.setter
    def despesas(self, valor):
        self.__despesas = valor
        self.__saldo = self.__receitas - self.despesas


    def adiciona_receita(self, valor):
        self.__receitas(self.receitas() + valor)

    def subtrai_receita(self, valor):
        self.__receitas(self.receitas() - valor)
        self.__saldo = self.__receitas - self.despesas
    


    
    