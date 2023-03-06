from enums import *
from Caracterizacion import *
from Personaje import *
from abc import ABC, abstractmethod

class AbstractBuilder(ABC):
    def withNombre(self, nombre: str):
        self._nombre = nombre

    def withVida(self, vida: int):
        self._vida = vida

    def withAtaque(self, ataque: int):
        self._ataque = ataque 
    
    def withLiga(self, liga: Liga):
        self._liga = liga 
    
    def withEnemigo(self, enemigo: Personaje):
        self._enemigo = enemigo 
    
    def withCaracterizacion(self, caracterizacion: Caracterizacion):
        self._caracterizacion = caracterizacion 

    @abstractmethod
    def build(self):
        pass

class HumanoBuilder(AbstractBuilder):
    def withNacionalidad(self, nacionalidad: Nacionalidad):
        self._nacionalidad = nacionalidad 

    def build(self):
        humano = Humano()
        humano.setNombre(self._nombre)
        humano.setVida(self._vida)
        humano.setAtaque(self._ataque)
        # humano.setLiga(self._liga)
        # humano.setEnemigo(self._enemigo)
        # humano.setCaracterizacion(self._caracterizacion)
        humano.setNacionalidad(self._nacionalidad)
        return humano

class SuperHumanoBuilder(AbstractBuilder):
    def build(self):
        superhumano = SuperHumano()
        superhumano.setNombre(self._nombre)
        superhumano.setVida(self._vida)
        superhumano.setAtaque(self._ataque)
        # humano.setLiga(self._liga)
        # humano.setEnemigo(self._enemigo)
        # humano.setCaracterizacion(self._caracterizacion)
        return superhumano

class ArtificialBuilder(AbstractBuilder):
    def withModelo(self, modelo: str):
        self._modelo = modelo 

    def build(self):
        artificial = Artificial()
        artificial.setNombre(self._nombre)
        artificial.setVida(self._vida)
        artificial.setAtaque(self._ataque)
        # humano.setLiga(self._liga)
        # humano.setEnemigo(self._enemigo)
        # humano.setCaracterizacion(self._caracterizacion)
        artificial.setModelo(self._modelo)
        return artificial

class AlienBuilder(AbstractBuilder):
    def withPlaneta(self, planeta: str):
        self._planeta = planeta 

    def build(self):
        alien = Alien()
        alien.setNombre(self._nombre)
        alien.setVida(self._vida)
        alien.setAtaque(self._ataque)
        # humano.setLiga(self._liga)
        # humano.setEnemigo(self._enemigo)
        # humano.setCaracterizacion(self._caracterizacion)
        alien.setPlaneta(self._planeta)
        return alien
