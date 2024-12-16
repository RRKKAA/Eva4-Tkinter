class Trabajador:
    def __init__(self, id_usuario:int, rut:str, nombre:str, apellido:str, sexo:str, direccion:str, telefono:int, cargo:str, area:str, departamento:str):
        self.id_usuario = id_usuario
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.direccion = direccion
        self.telefono = telefono
        self.cargo = cargo
        self.area = area
        self.departamento = departamento