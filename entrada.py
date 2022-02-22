class Entrada:
    def __init__(self, nombre, apellido, codigo, telefono, carrera):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__codigo = codigo
        self.__telefono = telefono
        self.__carrera = carrera

    def get_nombre(self): return self.__nombre
    def get_apellido(self): return self.__apellido
    def get_codigo(self): return self.__codigo
    def get_telefono(self): return self.__telefono
    def get_carrera(self): return self.__carrera

