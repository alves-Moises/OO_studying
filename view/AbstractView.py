from abc import ABC, abstractmethod

class AbstractView(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def receber_dados(self):
        pass

    @abstractmethod
    def mensagem_input(self, msg):
        return input(msg)

    @abstractmethod
    def mensagem_output(self, msg):
        print('=' *30)
        print('=' *30)
        print(msg)
