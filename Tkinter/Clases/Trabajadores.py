class Usuario:
    def __init__(self, rut, nombre, apellido, sexo, direccion, telefono, cargo, area, departamento, id_usuario=None):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.direccion = direccion
        self.telefono = telefono
        self.cargo = cargo
        self.area = area
        self.departamento = departamento
        self.id_usuario = id_usuario  # La FK que relaciona el trabajador a un usuario
        self.familiares = [] # aqui se almacenarian los objetos de la clase familiares

    def add_familiar(self, familiar):
        self.familiares.append(familiar)

    def remove_familiar(self, familiar):
        self.familiares.remove(familiar)