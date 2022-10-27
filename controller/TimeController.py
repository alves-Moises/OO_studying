from sqlite3 import Time
import controller.JogadorController
from controller.JogadorController import JogadorController
from controller.OrcamentoController import OrcamentoController
from view.TimeView import TimeView
from view.JogadorView import JogadorView

class TimeController():
    def __init__(self):
        # self.Jogadores = JogadorController()
        self.time = Time
        self.timeview = TimeView()
        self.jogadores = JogadorController()
        self.viewjogador = JogadorView()
    def opcoes(self):  #opcoes jogador
        print("Opcoes jogador")
        self.__escolhas = {
            "1": self.jogadores.listar_jogadores, 
            "2": OrcamentoController.ver_or,
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
               
            

    def tela_opcoes(self):
        print('asd')
        self.__escolhas = {
            "1": self.viewjogador.listar_jogadores,
            "2": "exibir_jogador especifico",
            "3": self.viewjogador.adicionar_jogador,
            "4": "remover_jogador"
        }
        escolha = self.viewjogador.tela_opcoes(self)
        if escolha == '1':
            JogadorController.listar_jogadores(self)

        if escolha == '2':
            pass

        if escolha == '3':
            JogadorController.jogadores =  JogadorController.adicionar_jogador(self)
        print('sucesso')
        self.__escolhas[self.__escolha](self)

    
       