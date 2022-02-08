from entity.Jogador import Jogador
import view.JogadorView
import view.AbstractView
# from controller import SystemController

class JogadorController():
    def __init__(self):
        self.__jogadores = []

    def adicionar_jogador(self):
        self.__nome = input("Digite o nome: ")
        self.__idade = int(input("digite idade: "))

        self.__jogador = Jogador(nome = self.__nome, idade = self.__idade)
        if (self.__jogador in self.__jogadores):
            view.JogadorView.exibir_mensagem("Atenção: Jogador já existe")
            return
        self.__jogadores.append(self.__jogador)

            
    def exibir_jogador(self, jogador):
        if jogador in self.__jogadores:
            view.JogadorView.JogadorView.exibir_jogador(jogador)
        else:
            view.JogadorView.exibir_mensagem("Atenção: Jogador não existe")

    def listar_jogadores(self):
        i = 0
        print(self.__jogadores)
        for jogador in self.__jogadores:
            print(i, 'ª:', end=' ')
            # view.JogadorView.JogadorView.exibir_jogador(jogador)
            i += 1

    def alterar_jogador(self, jogador):
        self.jogador.__nome = view.AbstractView.AbstractView.mensagem_input("Digite o nome: ")
        self.jogador.__idade = view.AbstractView.AbstractView.mensagem_input("Digite a idade: ")
        self.jogador.__posicao = view.AbstractView.AbstractView.mensagem_input("Digite a nova posicao: ")

    def remover_jogador(self, jogador):
        if jogador in self.__jogadores:
            self.__jogadores.pop(self.index(jogador))
            view.JogadorView.JogadorView.exibir_mensagem("Jogador removido com sucesso!")
            return
        view.JogadorView.JogadorView.exibir_mensagem("Jogador não existe...")


    def tela_opcoes(self):
        self.__escolhas = {
            "1": view.JogadorView.JogadorView.listar_jogadores,
            "2": "exibir_jogador especifico",
            "3": JogadorController.adicionar_jogador,
            "4": "remover_jogador"
        }
        self.__escolha = view.JogadorView.JogadorView.tela_opcoes(self)
        self.__escolhas[self.__escolha](self)
