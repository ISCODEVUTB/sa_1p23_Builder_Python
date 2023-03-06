# sa_1p23_Builder_Python
Builder - Python

# Estructura

El sistema está dividido tal que:

- `Personajes.py`: definiciones de la clase abstracta `Personaje` y sus subclases `Humano`, `SuperHumano`, `Artificial`, `Alien`.

- `Builder.py`: definiciones de la clase abstracta `AbstractBuilder` y sus subclases,
cada una dedicada específicamente a construir instancias de cada subclase de `Personajes`,
cumpliendo así uno de los principios SOLID de tener clases dedicadas a un solo propósito específico (no recuerdo el nombre exacto xd)

- `Caracterizacion.py`: definiciones de la clase abstracta `Caracterizacion` y sus distintas subclases.

- `Enum.py`: enumeraciones varias que usan para los atributos tanto de `Personaje` como de `Caracterizacion`.

En el archivo `main.py` se encuentra una instanciación ejemplo de distintas subclases de `Personaje` para validar el patrón de diseño utilizado.
