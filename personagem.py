
class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def exibir_status(self):
        print(f"Personagem:{self.nome}")
        print(f"Nível:{self.nivel}")
