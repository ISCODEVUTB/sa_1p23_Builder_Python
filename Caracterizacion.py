from abc import ABC, abstractmethod

class Caracterizacion(ABC):
    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def getDescripcion(self):
        return self._descripcion


class Poder(Caracterizacion):
    def setCosto(self, costo):
        self._costo = costo

    def getCosto(self):
        return self._costo

    def setDano(self, dano):
        self._dano = dano

    def getDano(self):
        return self._dano

    def setEfecto(self, efecto):
        self._efecto = efecto

    def getEfecto(self):
        return self._efecto

    def setAlcance(self, alcance):
        self._alcance = alcance

    def getAlcance(self):
        return self._alcance

    def setDuracion(self, duracion):
        self._duracion = duracion

    def getDuracion(self):
        return self._duracion

    def setTipo(self, tipo):
        self._tipo = tipo

    def getTipo(self):
        return self._tipo

    def setNivel(self, nivel):
        self._nivel = nivel

    def getNivel(self):
        return self._nivel

    def setReutilizacion(self, reutilizacion):
        self._reutilizacion = reutilizacion

    def getReutilizacion(self):
        return self._reutilizacion

    def setPrecision(self, precision):
        self._precision = precision

    def getPrecision(self):
        return self._precision

class Habilidad(Caracterizacion):
    def setCosto(self, costo):
        self._costo = costo

    def getCosto(self):
        return self._costo

    def setDano(self, dano):
        self._dano = dano

    def getDano(self):
        return self._dano

    def setEfecto(self, efecto):
        self._efecto = efecto

    def getEfecto(self):
        return self._efecto

    def setAlcance(self, alcance):
        self._alcance = alcance

    def getAlcance(self):
        return self._alcance

    def setDuracion(self, duracion):
        self._duracion = duracion

    def getDuracion(self):
        return self._duracion

    def setTipo(self, tipo):
        self._tipo = tipo

    def getTipo(self):
        return self._tipo

    def setNivel(self, nivel):
        self._nivel = nivel

    def getNivel(self):
        return self._nivel

    def setReutilizacion(self, reutilizacion):
        self._reutilizacion = reutilizacion

    def getReutilizacion(self):
        return self._reutilizacion

    def setPrecision(self, precision):
        self._precision = precision

    def getPrecision(self):
        return self._precision

class Debilidad(Caracterizacion):
    def setEfecto(self, efecto):
        self._efecto = efecto

    def getEfecto(self):
        return self._efecto

    def setDuracion(self, duracion):
        self._duracion = duracion

    def getDuracion(self):
        return self._duracion

    def setEstado(self, estado):
        self._estado = estado

    def getEstado(self):
        return self._estado

class Personalidad(Caracterizacion):
    def setRasgos(self, rasgos):
        self._rasgos = rasgos

    def getRasgos(self):
        return self._rasgos

    def setHumor(self, humor):
        self._humor = humor

    def getHumor(self):
        return self._humor


class Arma(Caracterizacion):
    def setDano(self, dano):
        self._dano = dano

    def getDano(self):
        return self._dano

    def setTipo(self, tipo):
        self._tipo = tipo

    def getTipo(self):
        return self._tipo

    def setAlcance(self, alcance):
        self._alcance = alcance

    def getAlcance(self):
        return self._alcance

    def setNivel(self, nivel):
        self._nivel = nivel

    def getNivel(self):
        return self._nivel

    def setPrecision(self, precision):
        self._precision = precision

    def getPrecision(self):
        return self._precision
