# Lara Marco
# Rol administrador

def rolAdmin():
    while True:
        print()
        print("-------------- Bienvenido Administrador --------------")
        print("------------------------------------------------------")
        print()
        print("Que desea hacer?")
        print(" 1. Agregar nuevas ciudades/puntos turisticos, distancias y costos")
        print(" 2. Listar las ciudades/puntos turisticos, distancias y costos")
        print(" 3. Consultar una ciudad/punto turistico, distancias y costos")
        print(" 4. Actualizar las ciudades/puntos turisticos")
        print(" 5. Eliminar las ciudades/puntos turisticos")
        print(" 6. Guardar las ciudades/puntos turisticos, distancias y costos en un archivo")
        print(" 7. Salir")
        opcionAdmin = int(input("Elija una opcion: "))

        match opcionAdmin:
            case 1:
                print("----- Ha seleccionado Agregar nuevas ciudades/puntos turisticos, distancias y costos ----- ")
            case 2:
                print("----- Ha seleccionado Agregar nuevas ciudades/puntos turisticos, distancias y costos ----- ")
            case 3:
                print("----- Ha seleccionado Agregar nuevas ciudades/puntos turisticos, distancias y costos ----- ")
            case 4:
                print("----- Ha seleccionado Agregar nuevas ciudades/puntos turisticos, distancias y costos ----- ")
            case 5:
                print("----- Ha seleccionado Agregar nuevas ciudades/puntos turisticos, distancias y costos ----- ")
            case 6:
                print("----- Ha seleccionado Agregar nuevas ciudades/puntos turisticos, distancias y costos ----- ")
            case 7:
                print("--- Saliendo del sistema --- ")
                break
            case _:
                print("Elija una opcion valida")
