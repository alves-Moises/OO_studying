from entity.Contrato import Contrato
from entity.Jogador import Jogador
from controller.ContratoController import ContratoController
from controller.JogadorController import JogadorController
from controller.TimeController import TimeController
import entity.Orcamento
import view.TimeView

class Time:
    def __init__(self, contratacoes: list[Contrato]):
        self.__view = view.TimeView.TimeView()
        self.__atributos = self.__view.iniciar()
        self.__nome = self.__atributos[0]
        self.__orcamento = entity.Orcamento.Orcamento(valor=self.__atributos[1])
        self.__contratacoes = contratacoes  #listar jogadores aqui
        # print(self.__nome)
        # print(self.__orcamento.saldo)

        self.__time_controller = TimeController()
        self.__time_controller.menu_principal()
        self.__contrato_controller = ContratoController()
        
    def contratar(self, jogador: Jogador, valor: float):
        if jogador in self.__contratacoes.jogador.nome:
            return

        contrato = self.__contrato_controller.novoContrato(valor=valor)
        jogador.__contrato = contrato(valor)
        self.__contratacoes.append(jogador)
        self.__orcamento.__adiciona_despesa = contrato.salario


    def rescindir(self, jogador: Jogador):
        
        # remover jogador do elenco
        #JogadorController.remover_jogador(jogador)
        
        # re-adicionar salario do total do orcamento
        self.__orcamento.despesas -= jogador.contrato.__salario
        self.__contratacoes.pop(jogador)
        
        