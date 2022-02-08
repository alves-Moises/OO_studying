class Contrato:

    def __init__(self, salario: float):
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    # #getter
    # @property
    # def contrato(self):
        pass
    #     return self.__contrato

    # #setter
    # @contrato.setter
    # def contrato(self, contrato):
    #     self.__contrato = contrato