from time import time
import controller.JogadorController
from controller.JogadorController import JogadorController
from controller.OrcamentoController import OrcamentoController
from view.TimeView import TimeView
class TimeController():
    def __init__(self):
        pass

    def menu_principal(self):
        self.__escolhas = {
            "1": JogadorController.tela_opcoes, 
            "2": TimeController.opcoes,
            }
            
        self.__menu = TimeView()
        self.__escolha = self.__menu.menu_principal()
        print(self.__escolha) # a escolha tá certa
        
        
        self.__escolhas[self.__escolha](self)
               
            

    def opcoes(self):
        self.__escolhas = {
            "1": JogadorController.listar_jogadores, 
            "2": OrcamentoController.ver_saldo,
            "3": "saldo",
            "4": "ver gastos"
            }
            
        self.__escolha = TimeView.opcoes()
        if self.escolha in self.__escolhas:
            self.__escolhas[self.__escolha](self)
            pass
        self.__escolhas[self.__escolha](self)
