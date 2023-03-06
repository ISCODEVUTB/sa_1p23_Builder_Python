from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self):
        self._caracterizacion = list()

    # Setters y getters
    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setVida(self, vida):
        self._vida = vida

    def getVida(self):
        return self._vida

    def setAtaque(self, ataque):
        self._ataque = ataque

    def getAtaque(self):
        return self._ataque

    def setLiga(self, liga):
        self._liga  = liga 

    def getLiga(self):
        return self._liga

    def setEnemigo(self, enemigo):
        self._enemigo = enemigo

    def getEnemigo(self):
        return self._enemigo

    def setCaracterizacion(self, caracterizacion):
        self._caracterizacion = caracterizacion

    def getCaracterizacion(self):
        return self._caracterizacion

    # Otros métodos 
    def atacar(self):
        print("{} realiza ataque".format(self._nombre))

    def recibirAtaque(self, dano: int):
        print("{} reacibe un ataque de {} de daño".format(self._nombre, dano))

class Humano(Personaje):
    def setNacionalidad(self, nacionalidad):
        self._nacionalidad = nacionalidad

    def getNacionalidad(self):
        return self._nacionalidad

class SuperHumano(Personaje):
    pass

class Artificial(Personaje):
    def setModelo(self, modelo):
        self._modelo = modelo

    def getModelo(self):
        return self._modelo

class Alien(Personaje):
    def setPlaneta(self, planeta):
        self._planeta = planeta

    def getPlaneta(self):
        return self._planeta
