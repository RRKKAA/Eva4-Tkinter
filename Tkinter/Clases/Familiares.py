class Familiar:
    def __init__(self, nombre, parentesco, sexo, rut, rut_trabajador):
        self.nombre = nombre
        self.parentesco = parentesco
        self.sexo = sexo
        self.rut = rut  # Clave primaria
        self.rut_trabajador = rut_trabajador

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    
    def set_parentesco(self, parentesco):
        self.parentesco = parentesco

    def get_parentesco(self):
        return self.parentesco
    
    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_sexo(self):
        return self.sexo
    
    def set_rut(self, rut):
        self.rut = rut

    def get_rut(self):
        return self.rut
    
    def set_rut_trabajador(self, rut_trabajador):
        self.rut_trabajador = rut_trabajador

    def get_rut_trabajador(self):
        return self.rut_trabajador