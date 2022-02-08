import controller.JogadorController

class JogadorView():

    def tela_opcoes(self):
        
        print("Selecione a opção desejada:")
        print("[1] Listar jogadores")
        print("[2] Exibir jogador específico")
        print("[3] Adicionar jogador")
        print("[4] Remover jogador")
        print("[0] fechar")
        return input()


    def listar_jogadores(self):
        print("Listando jogadores") 

        for jogador in controller.JogadorController.JogadorController.getJogadores():
            print(jogador)
        
    def exibir_jogador(self, jogador):
        if jogador in controller.JogadorController.jogadores:
            print(controller.JogadorController.exibir_jogador(jogador))
            return
        print("Jogador não encontrado")
    
    def exibir_mensagem(self, mensagem):
        print(mensagem)

