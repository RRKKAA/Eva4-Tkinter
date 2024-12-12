import bcrypt

class Usuario:
    def __init__(self, id, nombre_usuario, contrasena, rol):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.rol = rol

    def set_contrasena(self, nueva_contrasena):
        # Aplicar algoritmo de hash para encriptar la contraseña
        salt = bcrypt.gensalt()
        self.contrasena = bcrypt.hashpw(nueva_contrasena.encode('utf-8'), salt)

    def verificar_contrasena(self, contrasena_ingresada):
        return bcrypt.checkpw(contrasena_ingresada.encode('utf-8'), self.contrasena.encode('utf-8'))

    def __str__(self):
        return f"Usuario(id={self.id_usuario}, nombre={self.nombre_usuario}, rol={self.rol})"