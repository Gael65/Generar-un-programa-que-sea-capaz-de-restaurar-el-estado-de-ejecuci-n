from entrada import Entrada
import pickle

class Agenda:
    def __init__(self):
        try:
            with open("user_data", "rb") as agenda:
                self.__entradas = pickle.load(agenda)
            agenda.close()
        except:
            self.__entradas = []

    def agregar_entrada(self, nombre, apellido, codigo, telefono, carrera):
        entrada = Entrada(nombre, apellido, codigo, telefono, carrera)
        self.__entradas.append(entrada)
        self.__do_checkpoint()

    def eliminar_entrada(self, codigo):
        if len(self.__entradas) == 0:
            print("\nNo hay elementos en la agenda...")
        else:
            index = 0
            encontrado = False
            for entrada in self.__entradas:
                if entrada.get_codigo() == codigo:
                    index = self.__entradas.index(entrada)
                    self.__entradas.pop(index)
                    print("\nRegistro borrado de la agenda...")
                    encontrado = True
                    break
            if not encontrado:
                print("\nNo se encontraron coincidencias...")
            else:
                self.__do_checkpoint()
            
    def mostrar(self):
        #Visualizar el contenido de la lista de contactos
        print ("{:<8} {:<10} {:<10} {:<11} {:<4}".format("Nombre", "Apellido", "Codigo", "Telefono", "Carrera"))

        for entrada in self.__entradas:
            nombre, apellido, codigo, telefono, carrera = entrada.get_nombre(), entrada.get_apellido(), entrada.get_codigo(), entrada.get_telefono(), entrada.get_carrera()

            print ("{:<8} {:<10} {:<10} {:<11} {:<4}".format(nombre, apellido, codigo, telefono, carrera))
                
    def __do_checkpoint(self):
        #Serializar el estado del objeto (lista de contactos)
        if len(self.__entradas) > 0:
            with open("user_data", "wb") as agenda:
                pickle.dump(self.__entradas, agenda)
            agenda.close()
    