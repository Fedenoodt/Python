import sqlite3
from string import ascii_uppercase
Base_Usuarios = sqlite3.connect(r'C:\Users\Eduardo\Desktop\Accesos Directos\DB_Browser_for_SQLite\Ingreso_Usuario\Usuario.db')

def entrada():
    print('Interfaz de Ingreso al usuario')
    print('Ingrese su orden:')
    print('•1: Crear Usuario')
    print('•2: Ingresar')
    print('•3:Eliminar Usuario')

def opcion_1(Base_Usuarios):
    usuarioCreado = False
    usuario = ""

    caracteres_extraños = '!|"@·#$~%&¬/()=?¡¿<>-_,;.:´¨{ç}`^[+*]-.'
    numeros = '1234567890'
    print('Ingrese el nombre de usuario y contraseña para continuar...')

    nombreListo = False
    while nombreListo == False:
        usuario = input('Ingrese nombre de Usuario: ')
        for i in usuario:
            for j in ascii_uppercase:
                for k in caracteres_extraños:
                    if len(usuario) > 6:
                        print('¡Saludos,', usuario,'!')
                        nombreListo = True
                    else:
                        print('El nombre de usuario debe contener más de 6 carácteres, algúna mayúscula, y números o caracteres extraños.')
                        usuario = input('Vuelva a ingresar el Nombre de usuario: ')

    while usuarioCreado ==False:
        contraseña = input('Ingrese contraseña: ')
        contraseñaOK= input('Confirme la contraseña: ')
        if contraseñaOK == contraseña:
            INGRESO ='INSERT INTO Usuario (NOMBRE) VALUES("{}");'.format(usuario)
            usuarioCreado = True
            cursor = Base_Usuarios.cursor()
            cursor.execute(INGRESO)
            cursor.fetchall()
            Base_Usuarios.commit()
        else:
            print('Vuelva a ingresar la contraseña.')

opcion_1(Base_Usuarios)