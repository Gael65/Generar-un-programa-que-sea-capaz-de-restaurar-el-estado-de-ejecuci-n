from agenda import Agenda
import os

agenda = Agenda()

while True:
    #os.system("cls")
    agenda.mostrar()

    print("\n---------------Menu----------------")
    print("1. Añadir nueva entrada a la agenda")
    print("2. Borrar entrada de la agenda")
    print("0. Salir")

    opt = input("\nSelecciona una opcion: ")

    if opt == '1':
        nombre = input("Dame el nombre del alumno: ")
        apellido = input("Dame el apellido del alumno: ")
        codigo = input("Dame el codigo del alumno: ")
        telefono = input("Dame el telefono del alumno: ")
        carrera = input("Dame la carrera del alumno: ")

        agenda.agregar_entrada(nombre, apellido, codigo, telefono, carrera)

        print("\nRegistro agregado con exito a la agenda...")

        os.system("pause")

    elif opt == '2':
        codigo = input("Dame el codigo del estudiante a eliminar: ")
        agenda.eliminar_entrada(codigo)

        os.system("pause")

    elif opt == '0':
        break

    else:
        print("\nOpcion no valida...")

        os.system("pause")