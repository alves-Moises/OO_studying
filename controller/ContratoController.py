import entity.Contrato
import entity.Jogador

class ContratoController:
    def __init__(self):
        self.__contratos = []


    def novoContrato(self, valor:float, jogador:entity.Jogador.Jogador):
        novo_contrato = entity.Contrato.Contrato(valor)
        self.__contratos.append(novo_contrato)
        entity.Jogador.Jogador.contrato = novo_contrato

    def removerContrato(self, contrato=entity.Contrato.Contrato, jogador=entity.Jogador.Jogador):
        self.__contratos.pop(contrato)
        del(entity.Jogador.Jogador.contrato)