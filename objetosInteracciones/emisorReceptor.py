class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.dialogo = ''
        self.escuchar = ''
        self.habla = False

    def hablar(self,texto):
        self.dialogo = texto
        return

    def escucha(self,texto):
        self.escuchar = texto
        return


per1 = Persona('juan', 18)
per2 = Persona('Pedro', 31)

per1.hablar('que tal')

mensaje = per1.dialogo

per2.escucha(mensaje)

print(per2.escuchar)

