class Personaje:
    def __init__(self, nombre, vidas, poder):
        self.__nombre = nombre
        self.__vidas = vidas
        self.__poder = poder

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def vidas(self):
        return self.__vidas

    @vidas.setter
    def vidas(self, valor):
        self.__vidas = valor

    @property
    def poder(self):
        return self.__poder

    @poder.setter
    def poder(self, valor):
        self.__poder = valor

    def mover(self):
        print(f"{self.__nombre} se está moviendo.")

    def saltar(self):
        print(f"{self.__nombre} está saltando.")

    def caer(self):
        print(f"{self.__nombre} está cayendo.")


class Mario(Personaje):
    def __init__(self, nombre, vidas, poder, color="Rojo"):
        super().__init__(nombre, vidas, poder)
        self.color = color

    def lanzar_fuego(self):
        print(f"{self.nombre} está lanzando fuego.")


class Luigi(Personaje):
    def __init__(self, nombre, vidas, poder, color="Verde"):
        super().__init__(nombre, vidas, poder)
        self.color = color

    def usar_hongo(self):
        print(f"{self.nombre} está usando un hongo.")


class Enemigo:
    def __init__(self, nombre, tipo, danio):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__danio = danio

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    @property
    def danio(self):
        return self.__danio

    @danio.setter
    def poder(self, valor):
        self.__danio = valor

    def mover(self):
        print(f"El enemigo {self.__nombre} se está moviendo.")

    def atacar(self):
        print(f"El enemigo {self.__nombre} está atacando.")


class Koopa(Enemigo):
    def __init__(self, nombre, tipo, danio):
        super().__init__(nombre, tipo, danio)

    def usar_casco(self):
        print(f"El enemigo {self.nombre} se colocó un casco.")


class Goomba(Enemigo):
    def __init__(self, nombre, tipo, danio):
        super().__init__(nombre, tipo, danio)

    def esconder(self):
        print(f"El enemigo {self.nombre} se escondió.")


player1 = Mario("Jor", 3, 5)
player2 = Luigi("Lau", 4, 4)

enemigo1 = Koopa("Tortu", "Tortuga", 2)
enemigo2 = Goomba("Hongu", "Hongo", 1)

player1.saltar()
player2.mover()
enemigo1.usar_casco()
enemigo2.esconder()
print(enemigo2.nombre)
player1.lanzar_fuego()
player2.usar_hongo()
enemigo2.nombre = "Hon"
print(enemigo2.nombre)
enemigo1.atacar()
