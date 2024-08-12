class Coche:

    largoChasis = 250
    anchoChasis = 150
    ruedas = 4
    motor = 1600
    enMarcha = False

    def arrancar(self):
        if self.enMarcha == False:
            self.enMarcha = True
            return "El coche está ahora en marcha"
        else:
            return "El coche ya estaba en marcha, no se realizó acción"

    def estado(self):
        if self.enMarcha == True:
            return "El coche está en marcha"
        else:
            return "El coche está apagado"

    def apagar(self):
        if self.enMarcha == True:
            self.enMarcha = False
            return "El coche está ahora apagado"
        else:
            return "El coche ya estaba apagado, no se realizó acción"


miCoche = Coche()  # Instanciar una clase

print(f"El largo del coche es: {miCoche.largoChasis}")
print(f"El coche tiene {miCoche.ruedas} ruedas")

miCoche.arrancar()
print(miCoche.estado())
miCoche.apagar()
print(miCoche.estado())
