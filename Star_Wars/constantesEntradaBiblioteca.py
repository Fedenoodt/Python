import sqlite3

llamadaBiblioteca = sqlite3.connect('C:\Users\Eduardo\Desktop\Accesos Directos\DB Browser for SQLite\Ideas_Propias\Star Wars\Proyecto Biblioteca Jedi\Biblioteca.db')
c = llamadaBiblioteca.cursor()

def planetas():
    planeta = input('Ingrese planeta a la Biblioteca...     ')
    region = input('Ingrese región a la Biblioteca...     ')
    bioma = input('Ingrese el bioma del planeta a la Biblioteca...     ')
    descripcionBioma = input('Ingrese frase informativa de ese bioma a la Biblioteca...     ')
    clima = input('Mencione las caracteristicas básicas meteorológicas del planeta...     ')
    sistema = input('¿Se puede agregar el dato del sistema en el que está situado?     ')
    floraFauna = input('Algún dato interesante de su flora y/o fauna?     ')
    valorPlaneta = c.execute('INSERT INTO A_PLANETAS NOMBRE VALUES("{}");'.format(planeta))
    valorRegion = c.execute('INSERT INTO PLANETAS(REGION) VALUES("{}");'.format(region))
    valorBioma = c.execute('INSERT INTO BIOMA(NOMBRE) VALUES("{}");'.format(bioma))
    valorClima = c.execute('INSERT INTO CLIMA(PRINCIPALMENTE) VALUES("{}");'.format(clima))
    valorSistema = c.execute('INSERT INTO SISTEMAS(NOMBRE, REGION) VALUES("{}", "{}");'.format(sistema, region))
    valorFloraFauna = c.execute('INSERT INTO FLORAFAUNA(INFO) VALUES("{}");'.format(floraFauna))
    planeta = valorPlaneta
    region = valorRegion
    bioma = valorBioma
    descripcionBioma =
    return valorPlaneta, valorRegion, valorBioma,  valorClima, valorSistema, valorFloraFauna

def eras():
    nombre = input('¿De que era cronológica estamos hablando?     ')
    descripcion = input('Relate brevemente los susesos historicos...     ')
    valorEra = c.execute('INSERT INTO ERAS(NOMBRE, DESCRIPCION) VALUES("{}", "{}");'.format(nombre, descripcion))
    return valorEra

def personajes():
    nombre = input('Ingrese el nombre de esta figura...     ')
    apellido = input('¿Como se apellida?     ')
    valorPersonaje = c.execute('INSERT INTO PERSONAJES(NOMBRE, APELLIDO, RAZA_ID) VALUES("{}", "{}");'.format(nombre, apellido))
    razaCreada = input('¿La raza está creada? (Si/No)')

    if razaCreada == 'Si' or razaCreada == 'si' or razaCreada == 'SI' or razaCreada == 'sI':
        razaaAsignar = int(input('Ingrese ID de la Raza...     '))
        valorRaza1 = 'INSERT INTO RAZAS(ID) VALUES ("{}",);'.format(raza)
        return valorRaza1
    elif razaCreada == 'No' or razaCreada == 'no' or razaCreada == 'NO' or razaCreada == 'nO':
        razaNueva = input("Ingrese raza a la Biblioteca...     ")
        humanoide = 0
        humanoide = input("Ingrese 1 si la raza es humanoide, si no, un 0...     ")
    return valorPersonaje

def hechos():
    nombre = input('Ingrese el apodo con que se conoce al hecho...     ')
    descripcion = input('Cuente un poco sobre este suceso...     ')
    valorHecho = c.execute('INSERT INTO HECHOS(NOMBRE, DESCRIPCION, ERAS_ID) VALUES("{}", "{}");'.format(nombre, descripcion))
    eras_ID =  c.execute('INSERT INTO HECHOS(ERAS_ID) VALUES')
    return valorHecho

def naves():
    nombre = input('¿De que vehículo estamos hablando?     ')
    modelo = input('Diga el modelo, por favor...     ')
    descripcion = input('¿Algún detalle interesante sobre dicho modelo?     ')
    valorNave = c.execute('INSERT INTO NAVES(NOMBRE, MODELO_ID) VALUES("{}");'.format(nombre))
    valorModelo = c.execute('INSERT INTO MODELO(NOMBRE, DESCRIPCION) VALUES("{}", "{}");'.format(modelo, descripcion))
    return valorNave, valorModelo

cursodeAccion = [planetas(), personajes(), eras(), hechos(), naves()]