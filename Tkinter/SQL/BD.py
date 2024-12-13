import mysql.connector
import bcrypt
from Clases.Usuarios import Usuario

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

def registrar_usuario(nombre_usuario, contrasena_hasheada, rol):
    try:
        mydb, mycursor = conectar_db()

        # Insertar el usuario en la base de datos
        sql = "INSERT INTO usuarios (nombre_usuario, contrasena, rol) VALUES (%s, %s, %s)"
        val = (nombre_usuario, contrasena_hasheada, rol)
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
                return Usuario(resultado[0], resultado[1], resultado[2], resultado[3])
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