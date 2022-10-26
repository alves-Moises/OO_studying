from sqlite3 import Time
import controller.JogadorController
from controller.JogadorController import JogadorController
from controller.OrcamentoController import OrcamentoController
from view.TimeView import TimeView

class TimeController():
    def __init__(self):
        # self.Jogadores = JogadorController()
        self.time = Time
        self.timeview = TimeView()
        self.jogadores = JogadorController()
        
    def opcoes(self):  #opcoes jogador
        print("Opcoes jogador")
        self.__escolhas = {
            "1": self.jogadores.listar_jogadores, 
            "2": OrcamentoController.ver_saldo,
            "3": OrcamentoController.ver_saldo,
            "4": "ver gastos"
            }

        # pega escolha e executar o comando
        self.__escolha = self.timeview.opcoes()
        if self.__escolha in self.__escolhas:
            self.__escolhas[self.__escolha]()

        # if self.__escolha == '3':
        #     OrcamentoController.ver_saldo(self, Time)

    def menu_principal(self):  #menu inicial
        print("Menu principal")
        self.__escolhas = {
            "1": JogadorController.tela_opcoes,  #jogador opcoes
            "2": TimeController.opcoes   #time opcoes
            }
            
        self.__menu = TimeView()
        self.__escolha = self.__menu.menu_principal()
        print(self.__escolha) # a escolha tá certa
        
        
        self.__escolhas[self.__escolha](self)
               
            


       