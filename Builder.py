from Caracterizacion import *
from Personaje import *
from abc import ABC, abstractmethod

class AbstractBuilder(ABC):
    @abstractmethod
    def build(self):
        pass
