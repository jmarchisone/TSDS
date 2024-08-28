import random


class Dado:
    caras = 6

    def __init__(self, caras):
        self.caras = caras

    def lanzar(self):
        numero = random.randint(1, self.caras)
        print(f"Sacaste un {numero}")


dado = Dado(20)

dado.lanzar()
