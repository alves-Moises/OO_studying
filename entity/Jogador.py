class Jogador:

    def __init__(self, nome='teste', idade=123, posicao='reserva'):
        self.__nome = nome
        self.__idade = idade
        self.__contrato = None
        self.__posicao = posicao

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
    