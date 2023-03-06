# sa_1p23_Builder_Python
Builder - Python

# Estructura

El sistema está dividido tal que:

- `Personajes.py`: definiciones de la clase abstracta `Personaje` y sus subclases `Humano`, `SuperHumano`, `Artificial`, `Alien`.

- `Caracterizacion.py`: definiciones de la clase abstracta `Caracterizacion` y sus distintas subclases.

- `Builder.py`: definición de la clase abstracta `AbstractBuilder`.

- `PersonajeBuilder.py`: definiciones de las subclases de `AbstractBuilder` relacionadas con las subclases de `Personaje`,
cada una dedicada específicamente a construir instancias de su respectiva subclase.

- `CaracterizacionBuilder.py`: definiciones de las subclases de `AbstractBuilder` relacionadas con las subclases de `Caracterizacion`,
cada una dedicada específicamente a construir instancias de su respectiva subclase.

- `IFicha.py`: definición de la interfaz `IFicha` dedicada a añadir caracterizaciones, liga y enemigos a un `Personaje`.

- `Enum.py`: enumeraciones varias que usan para los atributos tanto de `Personaje` como de `Caracterizacion`.

En el archivo `main.py` se encuentra una instanciación ejemplo de distintas subclases de `Personaje` para validar el patrón de diseño utilizado.

Pendiente:

- Implementar Director que use `IFicha` y los Builders.
