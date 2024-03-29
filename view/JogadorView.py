import controller.JogadorController

class JogadorView():
    def __init__():
        pass

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
        controller.JogadorController.JogadorController.getJogadores(self)
        for jogador in controller.JogadorController.JogadorController.getJogadores(self):
            print(jogador)
        
    def exibir_jogador(self, jogador):
        if jogador in controller.JogadorController.jogadores:
            print(controller.JogadorController.exibir_jogador(self, jogador))
            return
        print("Jogador não encontrado")
    
    def exibir_mensagem(self, mensagem):
        print('=' * 30)
        print(mensagem)
        print('=' * 30)

