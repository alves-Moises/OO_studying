from entity.Jogador import Jogador
import view.JogadorView
import view.AbstractView
# from controller import JogadorController
# from controller import SystemController
    
class JogadorController():
    def __init__(self):
        self.__jogadores = list()


    # def getJogadores(self):
    #     return self.__jogadores
    @property
    def jogadores(self):
        return self.__jogadores

    @jogadores.setter
    def jogadores(self, jogador):
        self.__jogadores += jogador

    def adicionar_jogador(self):
        self.__name = input("Digite o nome: ")
        self.__age = int(input("digite idade: "))
        self.__position = input("Digite a posicao: ")

        self.__jogador = Jogador(nome = self.__name, idade = self.__age, posicao=self.__position)
        # print(self.__jogador.nome)
        self.__jogadores.setter(self, self.__jogador)
        return self.__jogador
        print('Jogador adicionado com sucesso')

            
    def exibir_jogador(self, jogador):
        if jogador in self.__jogadores:
            view.JogadorView.JogadorView.exibir_jogador(jogador)
        else:
            view.JogadorView.exibir_mensagem("Atenção: Jogador não existe")

    def listar_jogadores(self):
        i = 0
        if self.__jogadores == []:
            view.AbstractView.AbstractView.mensagem_output("Lista de jogadores vazia.")
        # for jogador in self.__jogadores:
        #     print(i, 'ª:', end=' ')
        #     # view.JogadorView.JogadorView.exibir_jogador(jogador)
        #     i += 1

    def alterar_jogador(self, jogador):
        self.jogador.__nome = view.AbstractView.AbstractView.mensagem_input("Digite o nome: ")
        self.jogador.__idade = view.AbstractView.AbstractView.mensagem_input("Digite a idade: ")
        self.jogador.__posicao = view.AbstractView.AbstractView.mensagem_input("Digite a nova posicao: ")
        self.jogador.__camisa = view.AbstractView.AbstractView.mensagem_input("Digite o numero da camisa: ")

    def remover_jogador(self, jogador):
        if jogador in self.__jogadores:
            self.__jogadores.pop(self.index(jogador))
            view.JogadorView.JogadorView.exibir_mensagem("Jogador removido com sucesso!")
            return
        view.JogadorView.JogadorView.exibir_mensagem("Jogador não existe...")


    def tela_opcoes(self):
        print('asd')
        self.__escolhas = {
            "1": view.JogadorView.JogadorView.listar_jogadores,
            "2": "exibir_jogador especifico",
            "3": JogadorController.adicionar_jogador,
            "4": "remover_jogador"
        }
        if view.JogadorView.JogadorView.tela_opcoes(self) == '1':
            JogadorController.listar_jogadores(self)

        if view.JogadorView.JogadorView.tela_opcoes(self) == '2':
            pass

        if view.JogadorView.JogadorView.tela_opcoes(self) == '3':
            JogadorController.jogadores =  JogadorController.adicionar_jogador(self)
        print('sucesso')
        self.__escolhas[self.__escolha](self)

    