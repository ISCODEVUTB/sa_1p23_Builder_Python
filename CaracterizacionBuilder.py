from enums import *
from Caracterizacion import *
from Personaje import *
from Builder import *

class AbstractCaracterizacionBuilder(AbstractBuilder):
    def withNombre(self, nombre: str):
        self._nombre = nombre

    def withDescripcion(self, descripcion: str):
        self._descripcion = descripcion

    @abstractmethod
    def build(self):
        pass

class PoderBuilder(AbstractCaracterizacionBuilder):
    def withCosto(self, costo):
        self._costo = costo

    def withDano(self, dano):
        self._dano = dano

    def withEfecto(self, efecto):
        self._efecto = efecto

    def withAlcance(self, alcance):
        self._alcance = alcance

    def withDuracion(self, duracion):
        self._duracion = duracion

    def withTipo(self, tipo):
        self._tipo = tipo

    def withNivel(self, nivel):
        self._nivel = nivel

    def withReutilizacion(self, reutilizacion):
        self._reutilizacion = reutilizacion

    def withPrecision(self, precision):
        self._precision = precision

    def build(self):
        poder = Poder()
        poder.setNombre(self._nombre)
        poder.setDescripcion(self._descripcion)
        poder.setCosto(self._costo)
        poder.setDano(self._dano)
        poder.setEfecto(self._efecto)
        poder.setAlcance(self._alcance)
        poder.setDuracion(self._duracion)
        poder.setTipo(self._tipo)
        poder.setNivel(self._nivel)
        poder.setReutilizacion(self._reutilizacion)
        poder.setPrecision(self._precision)
        return poder

class HabilidadBuilder(AbstractCaracterizacionBuilder):
    def withCosto(self, costo):
        self._costo = costo

    def withDano(self, dano):
        self._dano = dano

    def withEfecto(self, efecto):
        self._efecto = efecto

    def withAlcance(self, alcance):
        self._alcance = alcance

    def withDuracion(self, duracion):
        self._duracion = duracion

    def withTipo(self, tipo):
        self._tipo = tipo

    def withNivel(self, nivel):
        self._nivel = nivel

    def withReutilizacion(self, reutilizacion):
        self._reutilizacion = reutilizacion

    def withPrecision(self, precision):
        self._precision = precision

    def build(self):
        habilidad = Habilidad()
        habilidad.setNombre(self._nombre)
        habilidad.setDescripcion(self._descripcion)
        habilidad.setCosto(self._costo)
        habilidad.setDano(self._dano)
        habilidad.setEfecto(self._efecto)
        habilidad.setAlcance(self._alcance)
        habilidad.setDuracion(self._duracion)
        habilidad.setTipo(self._tipo)
        habilidad.setNivel(self._nivel)
        habilidad.setReutilizacion(self._reutilizacion)
        habilidad.setPrecision(self._precision)
        return habilidad

class DebilidadBuilder(AbstractCaracterizacionBuilder):
    def withEfecto(self, efecto):
        self._efecto = efecto

    def withDuracion(self, duracion):
        self._duracion = duracion

    def withEstado(self, estado):
        self._estado = estado

    def build(self):
        debilidad = Debilidad()
        debilidad.setNombre(self._nombre)
        debilidad.setDescripcion(self._descripcion)
        debilidad.setEfecto(self._efecto)
        debilidad.setDuracion(self._duracion)
        debilidad.setEstado(self._estado)
        return debilidad 

class PersonalidadBuilder(AbstractCaracterizacionBuilder):
    def withRasgos(self, rasgos):
        self._rasgos = rasgos

    def withHumor(self, humor):
        self._humor = humor

    def build(self):
        personalidad = Personalidad()
        personalidad.setNombre(self._nombre)
        personalidad.setDescripcion(self._descripcion)
        personalidad.setRasgos(self._rasgos)
        personalidad.setHumor(self._humor)
        return personalidad

class ArmaBuilder(AbstractCaracterizacionBuilder):
    def withDano(self, dano):
        self._dano = dano

    def withTipo(self, tipo):
        self._tipo = tipo

    def withAlcance(self, alcance):
        self._alcance = alcance

    def withNivel(self, nivel):
        self._nivel = nivel

    def withPrecision(self, precision):
        self._precision = precision

    def build(self):
        arma = Arma()
        arma.setNombre(self._nombre)
        arma.setDescripcion(self._descripcion)
        arma.setDano(self._dano)
        arma.setTipo(self._tipo)
        arma.setAlcance(self._alcance)
        arma.setNivel(self._nivel)
        arma.setPrecision(self._precision)
        return arma
