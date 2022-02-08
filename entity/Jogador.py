class Jogador:

    def __init__(self, nome: str, idade: float, contrato=None, posicao='reserva'):
        self.__nome = nome
        self.__idade = idade
        self.__posicao = posicao
        self.__contrato = contrato

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def contrato(self):
        return self.__contrato

    @contrato.setter
    def contrato(self, contrato):
        self.__contrato = contrato
    
    @contrato.deleter
    def contrato(self):
        self.__contrato = None

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao
    