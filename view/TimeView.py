

class TimeView():   
    def __init__(self):
        pass

    def opcoes(self):
        print("Selecione a opção desejada")
        print("[1] Listar_jogadores")
        print("[2] Ver orçamento")
        print("[3] Ver saldo")
        print("[4] Ver gastos")
        return input()

    def iniciar(self):
        self.__nome = input("Digite o nome do time: ")
        self.__orcamento = float(input("Digite o orcamento inical: ")) 
        return [self.__nome, self.__orcamento]
    
    def menu_principal(self):
        print("Menu principal: ")
        print("[1] Opcões jogadores")
        print("[2] Opcões time")
        print("[3] Adicionar jogador")
        print("[4] Listar jogadores")
        print("[0] Fechar")
        return input()