from PersonajeBuilder import *
from IFicha import *

# Instancias de ejemplo
hb = HumanoBuilder()
hb.withNombre("Batman")
hb.withVida(100)
hb.withAtaque(10)
hb.withNacionalidad(Nacionalidad(1))

batman = hb.build()
batman.atacar()
batman.recibirAtaque(5)

hb.withNombre("Joker")
hb.withVida(100)
hb.withAtaque(10)
hb.withNacionalidad(Nacionalidad(1))
joker = hb.build()

ab = AlienBuilder()
ab.withNombre("Superman")
ab.withVida(100)
ab.withAtaque(10)
ab.withPlaneta("Kripton")

superman = ab.build()
superman.atacar()
superman.recibirAtaque(5)

ificha = IFicha()
ificha.Enemigo(batman, superman)
ificha.Enemigo(batman, joker)

print("Los enemigos de Batman son:")
for e in batman.getEnemigo():
    print(e.getNombre())


