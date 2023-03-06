from enums import *
from Personaje import *
from Caracterizacion import *

class IFicha():
    def Add(self, personaje: Personaje, caracterizacion: Caracterizacion):
        personaje.setCaracterizacion(caracterizacion)

    def Liga(self, personaje: Personaje, liga: Ligas):
        personaje.setLiga(liga)

    def Enemigo(self, personaje: Personaje, enemigo: Personaje):
        personaje.setEnemigo(enemigo)
