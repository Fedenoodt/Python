class Persona:
    def __init__(self, nombre, edad, estatura, especie, peso, posicion):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.especie = especie
        self.peso = peso
        self.posicion = posicion

    def correr(self, tiempo):
        velocidad = self.peso / 3
        paso = velocidad * tiempo / 2
        corrida = paso / tiempo + 3/4 * self.estatura
        print('En ' + str(tiempo) + ' segundos, ' + str(self.nombre) + ' corrió ' + str(int(corrida)) + ' pasos.')

Persona1 = Persona('Ahsoka', 18, 1.7, 'togruta', 54, 0)

Persona2 = Persona('Anakin', 20, 1.88, 'humano', 84, 0)

Persona1.correr(20)
Persona2.correr(15)

if Persona2.nombre == 'Anakin':
    print('Estás en este consejo, pero no te concedemos el rango de maestro.')