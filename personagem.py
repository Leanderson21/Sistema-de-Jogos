
class Personagem:
    def __init__(self, nome, nivel):
        self.__nome = nome
        if nivel > 0:
            self.nivel = nivel
        else:
            print("Nível precisa ser maior que 0, definindo o nível para 1")
            self.__nivel = 1

    def exibir_status(self):
        print(f"Personagem:{self.__nome}")
        print(f"Nível:{self.__nivel}")

    def get_nome(self):
        return self.__nome
    def set_nome(self,nome):
        self.__nome = nome
    def get_nivel(self):
        return self.__nivel
    def set_nivel(self,nivel):
        if nivel > 0:
            self.__nivel = nivel
        else:
            print("O nível não pode ser menor que 0")
