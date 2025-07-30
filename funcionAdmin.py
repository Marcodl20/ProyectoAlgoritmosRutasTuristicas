# Lara Marco
# Rol administrador
import heapq

grafoDistancias = {
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

grafoPrecios = {
    'Tulcan': [('Ibarra', 25)],
    'Ibarra': [('Tulcan', 25), ('Quito', 20)],
    'Quito': [('Ibarra', 20), ('SantoDomingo', 15), ('Ambato', 35), ('Tena', 27)],
    'SantoDomingo': [('Quito', 15), ('Esmeraldas', 10), ('Manta', 19), ('Guayaquil', 18)],
    'Esmeraldas': [('SantoDomingo', 10)],
    'Manta': [('SantoDomingo', 19), ('Guayaquil', 27)],
    'Guayaquil': [('SantoDomingo', 18), ('Ambato', 14), ('Cuenca', 26), ('Machala', 40), ('Manta', 27)],
    'Ambato': [('Quito', 35), ('Macas', 21), ('Guayaquil', 14), ('Cuenca', 13)],
    'Tena': [('Quito', 27), ('Macas', 12)],
    'Macas': [('Tena', 12), ('Ambato', 21)],
    'Cuenca': [('Ambato', 13), ('Loja', 16), ('Machala', 11), ('Guayaquil', 26)],
    'Loja': [('Cuenca', 16), ('Machala', 41)],
    'Machala': [('Guayaquil', 40), ('Cuenca', 11), ('Loja',41)]
}

# Metodo de Ordenamiento (Burbuja)
def ordenarListaCiudades(rutas, criterio):
    tamanio = len(rutas)

    for i in range(tamanio -1):
        for j in range(tamanio -1 - i):
            if rutas[j][criterio] > rutas[j + 1][criterio]:
                rutas[j], rutas[j + 1] = rutas[j + 1], rutas[j]
    return rutas


# Metodo Para Listar las Ciudades sin duplicados y ordenada por distancias
def listarCiudades(grafoDistancias, grafoPrecios):
    mostrarConexiones = set()
    rutas = []

    for ciudadOrigen in grafoDistancias:
        conexionesDistancia = grafoDistancias[ciudadOrigen]
        conexionesPrecio = grafoPrecios.get(ciudadOrigen, [])

        preciosDestino = {ciudadDestino: precio for ciudadDestino, precio in conexionesPrecio}

        for ciudadDestino, distancia in conexionesDistancia:
            conexion = tuple(sorted([ciudadOrigen, ciudadDestino]))

            if conexion not in mostrarConexiones:
                mostrarConexiones.add(conexion)
                precio = preciosDestino.get(ciudadDestino, "No disponible")

                rutas.append({
                    "origen": ciudadOrigen,
                    "destino": ciudadDestino,
                    "distancia": distancia,
                    "precio": precio
                })

    rutas = ordenarListaCiudades(rutas, "distancia")
    for ruta in rutas:
        print(f"{ruta['origen']} <-----> {ruta['destino']}, Distancia: {ruta['distancia']} km, Precio: {ruta['precio']} $")
    







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
                    listarCiudades(grafoDistancias, grafoPrecios)

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