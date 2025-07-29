# Lara Marco
# Rol administrador
grafo = {
    'Tulcan': [('Ibarra', 126)],
    'Ibarra': [('Tulcan', 126), ('Quito', 113)],
    'Quito': [('Ibarra', 113), ('SantoDomingo', 152), ('Ambato', 151), ('Tena', 192)],
    'SantoDomingo': [('Quito', 152), ('Esmeraldas', 180), ('Manta', 245), ('Guayaquil', 282)],
    'Esmeraldas': [('SantoDomingo', 180)],
    'Manta': [('SantoDomingo', 245), ('Guayaquil', 195)],
    'Guayaquil': [('SantoDomingo', 282), ('Ambato', 276), ('Cuenca', 196), ('Machala', 183), ('Manta', 195)],
    'Ambato': [('Quito', 151), ('Macas', 214), ('Guayaquil', 276), ('Cuenca', 308)],
    'Tena': [('Quito', 192), ('Macas', 204)],
    'Macas': [('Tena', 204), ('Ambato', 214)],
    'Cuenca': [('Ambato', 308), ('Loja', 212), ('Machala', 169), ('Guayaquil', 196)],
    'Loja': [('Cuenca', 212), ('Machala', 237)],
    'Machala': [('Guayaquil', 183), ('Cuenca', 169), ('Loja',237)]
}


def rolAdmin():
    while True:
        try:
            print()
            print("-------------- Bienvenido Administrador --------------")
            print("------------------------------------------------------")
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
                    print("----- Ha seleccionado Listar las ciudades/puntos turisticos, distancias y costos ----- ")
                case 3:
                    print("----- Ha seleccionado Consultar una ciudad/punto turistico, distancias y costos ----- ")
                case 4:
                    print("----- Ha seleccionado Actualizar las ciudades/puntos turisticos ----- ")
                case 5:
                    print("----- Ha seleccionado Eliminar las ciudades/puntos turisticos ----- ")
                case 6:
                    print("----- Guardar las ciudades/puntos turisticos, distancias y costos en un archivo ----- ")
                case 7:
                    print("--- Saliendo del sistema --- ")
                    break
                case _:
                    print("Elija una opcion valida")
        except ValueError:
            print("Valores invalidos, por favor intente nuevamente")

rolAdmin()