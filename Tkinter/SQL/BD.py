import mysql.connector
import bcrypt
from Clases.Usuarios import Usuario
from Clases.Trabajadores import Trabajador

def conectar_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Jujuy"
        )
        mycursor = mydb.cursor()
        return mydb, mycursor
    except mysql.connector.Error as error:
        print(f"Error al conectar a la base de datos: {error}")

def registrar_usuario(nombre_usuario, contrasena_hasheada, rol, rut_usuario):
    try:
        mydb, mycursor = conectar_db()

        # Insertar el usuario en la base de datos
        sql = "INSERT INTO usuarios (nombre_usuario, contrasena, rol, rut_usuario) VALUES (%s, %s, %s, %s)"
        val = (nombre_usuario, contrasena_hasheada, rol, rut_usuario)
        mycursor.execute(sql, val)
        mydb.commit()

        print("Usuario registrado correctamente")
    except mysql.connector.Error as error:
        print(f"Error al registrar usuario: {error}")
    finally:
        if mydb:
            mydb.close()

def verificar_usuario(nombre_usuario, contrasena):
    try:
        mydb, mycursor = conectar_db()
        sql = "SELECT * FROM Usuarios WHERE nombre_usuario = %s"
        val = (nombre_usuario,)
        mycursor.execute(sql, val)
        resultado = mycursor.fetchone()

        if resultado:
            if bcrypt.checkpw(contrasena.encode('utf-8'), resultado[2].encode('utf-8')):
                return Usuario(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
            else:
                return None
        else:
            return None
    except mysql.connector.Error as error:
        print(f"Error al verificar usuario: {error}")
        return None
    finally:
        if mydb:
            mydb.close()


def insertar_trabajador(rut, nombre, apellido, sex, direccion, telefono, cargo, area, departamento):
    try:
        mydb, mycursor = conectar_db()

        sql = "INSERT INTO trabajadores (rut, nombre, apellido, sexo, direccion, telefono, cargo, area, departamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (rut, nombre, apellido, sex, direccion, telefono, cargo, area, departamento)
        mycursor.execute(sql, val)
        mydb.commit()

        print("Usuario registrado correctamente")
    except mysql.connector.Error as error:
        print(f"Error al registrar usuario: {error}")
    finally:
        if mydb:
            mydb.close()



def obtener_trabajadores():
    try:
        mydb, mycursor = conectar_db()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM trabajadores")
        resultados = mycursor.fetchall()
        trabajadores = []
        for row in resultados:
            # Crear un objeto Trabajador por cada fila
            trabajador = Trabajador(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            trabajadores.append(trabajador)

        return trabajadores
    except mysql.connector.Error as error:
        print(f"Error al registrar usuario: {error}")
    finally:
        if mydb:
            mydb.close()
    
def obtener_trabajador_por_rut(rut):
    try:
        mydb, mycursor = conectar_db()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM trabajadores WHERE rut = %s", (rut,))
        resultado = mycursor.fetchone()
        if resultado:
            trabajador = Trabajador(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6], resultado[7], resultado[8], resultado[9])

        return trabajador
        
    except mysql.connector.Error as error:
        print(f"Error al obtener los trabajadores: {error}")
        return []
    finally:
        if mydb:
            mydb.close()

def obtener_ruts_disponibles():
    try:
        mydb, mycursor = conectar_db()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT rut_usuario FROM usuarios WHERE rol = 'trabajador' AND rut_usuario NOT IN (SELECT rut FROM trabajadores)")
        resultados = [row[0] for row in mycursor.fetchall()] #mycursor.fetchall()
        return resultados
    except mysql.connector.Error as error:
        print(f"Error al obtener los trabajadores: {error}")
        return []
    finally:
        if mydb:
            mydb.close()