# Lara Marco
# Rol administrador
import heapq
import os

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

# Carga la lista de rutas desde el archivo rutas.txt
def cargarRutas():
    rutas = []
    if not os.path.exists("rutas.txt"):
        return rutas
    
    with open("rutas.txt", "r") as archivo:
        for linea in archivo:
            try:
                partes = linea.strip().split(", ")
                origen = partes[0].split(": ")[1]
                destino = partes[1].split(": ")[1]
                distancia = float(partes[2].split(": ")[1])
                precio = float(partes[3].split(": ")[1])

                rutas.append({
                    "origen": origen,
                    "destino": destino,
                    "distancia": distancia,
                    "precio": precio
                })
            except Exception:
                print(f"Formato invalido en la linea: {linea.strip()}")
    return rutas

# Funcion para Agregar una Ruta
def agregarRuta(grafoDistancias, grafoPrecios):
    try:
        origen = input("Ingrese el nombre de la ciudad de Inicio (origen): ")
        destino = input("Ingrese el nombre de la ciudad de Destino: ")
        distancia = float(input("Ingrese la distancia que hay entre las dos ciudades: "))
        precio = float(input("Ingrese el precio de la ruta: "))

    except ValueError:
        print("Datos invalidos, intente nuevamente")
        return
        
    grafoDistancias.setdefault(origen, []).append((destino, distancia))
    grafoDistancias.setdefault(destino, []).append((origen, distancia))

    grafoPrecios.setdefault(origen, []).append((destino, precio))
    grafoPrecios.setdefault(destino, []).append((origen, precio))

    print("Ruta Agregada Correctamente")

# Funcion Para Listar las Ciudades sin duplicados y ordenada por distancias
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

# Funcion para consultar una Ruta
def consultarRuta(grafoDistancias, grafoPrecios):
    ciudadConsulta = input("Ingrese el nombre de la ciudad que desea consultar: ")

    encontrado = False

    # Algoritmo de Busqueda Lineal
    for ciudad in grafoDistancias:
        if ciudad == ciudadConsulta:
            print(f"Rutas desde {ciudadConsulta}:")
            conexiones = grafoDistancias.get(ciudadConsulta, [])
            preciosDestino = dict(grafoPrecios.get(ciudadConsulta, []))

            for destino, distancia in conexiones:
                precio = preciosDestino.get(destino, "No disponible")
                print(f"{ciudadConsulta} <-----> {destino}, Distancia: {distancia} Km, Precio: {precio} $")
            
            encontrado = True
            break
    
    if not encontrado:
        print("No hay rutas registradas para esa ciudad")

# Funcion para actualizar rutas
def actualizarRuta(grafoDistancias, grafoPrecios):
    origenActualizar = input("Ingrese la ciudad de origen que quiera actualizar: ").strip().title()
    destinoActualizar = input("Ingrese la ciudad de destino que quiera actualizar: ").strip().title()

    if origenActualizar in grafoDistancias and destinoActualizar in grafoDistancias:
        actualizo = False

        print("Que desea modificar?")
        print(" 1. Distancia \n 2. Precio")
        try:
            opcion = int(input("Elija una opción: "))
            match opcion:
                case 1:
                    nuevaDistancia = float(input("Ingrese la nueva distancia (Km): "))
                    grafoDistancias[origenActualizar] = [
                        (ciudad, nuevaDistancia if ciudad == destinoActualizar else distancia)
                        for ciudad, distancia in grafoDistancias[origenActualizar]
                    ]

                    grafoDistancias[destinoActualizar] = [
                        (ciudad, nuevaDistancia if ciudad == origenActualizar else distancia)
                        for ciudad, distancia in grafoDistancias[destinoActualizar]
                    ]

                    actualizo = True
                case 2:
                    nuevoPrecio = float(input("Ingrese el nuevo precio ($): "))
                    grafoPrecios[origenActualizar] = [
                        (ciudad, nuevoPrecio if ciudad == destinoActualizar else precio)
                        for ciudad, precio in grafoPrecios[origenActualizar]
                    ]

                    grafoPrecios[destinoActualizar] = [
                        (ciudad, nuevoPrecio if ciudad == origenActualizar else precio)
                        for ciudad, precio in grafoPrecios[destinoActualizar]
                    ]
                    actualizo = True
                case _:
                    print("Valor fuera de rango, intente nuevamente")
        except ValueError:
            print("Valores invalidos, intente nuevamente")
        
        if actualizo:
            print("ruta actualizada Correctamente")
    else:
        print("Ciudad de origen(inicio) no encontrada")

# Funcion para Eliminar ciudades/ruta
def eliminarRuta(grafoDistancias, grafoPrecios):
    ciudadEliminar = input("Ingrese el nombre de la ciudad que desea eliminar su ruta: ")

    if ciudadEliminar in grafoDistancias:
        print(f"Se eliminaran todas las rutas de {ciudadEliminar}")
        del grafoDistancias[ciudadEliminar]
        del grafoPrecios[ciudadEliminar]

        for ciudad in grafoDistancias:
            grafoDistancias[ciudad] = [(destino, distancia) for destino, distancia in grafoDistancias[ciudad]
                                    if destino != ciudadEliminar]
            
            grafoPrecios[ciudad] = [(destino, precio) for destino, precio in grafoPrecios[ciudad]
                                    if destino != ciudadEliminar]
            
        print("Ruta(s) eliminada(s) correctamente")

    else:
        print("No hay rutas registradas para esa ciudad")

# Funcion para Guardar Rutas
def guardarRutas(grafoDistancias, grafoPrecios):
    rutas = []
    rutasGuardadas = set()

    for origen in grafoDistancias:
        conexionesDistancia = grafoDistancias[origen]
        conexionesPrecio = dict(grafoPrecios.get(origen, []))

        for destino, distancia in conexionesDistancia:
            rutaOrdenada = tuple(sorted([origen, destino]))

            if rutaOrdenada not in rutasGuardadas:
                rutasGuardadas.add(rutaOrdenada)
                precio = conexionesPrecio.get(destino, "No disponible")

                rutas.append({
                    "origen": origen,
                    "destino": destino,
                    "distancia": distancia,
                    "precio": precio
                })

    rutas = ordenarListaCiudades(rutas, "distancia")

    with open("rutas.txt", "w") as archivo:
        for ruta in rutas:
            archivo.write(f"Ciudad de inicio: {ruta['origen']} <-----> Destino: {ruta['destino']}, Distancia: {ruta['distancia']} km, Precio: {ruta['precio']} $ \n")


    print("Cambios Guardados correctamente en el archivo 'rutas.txt'")

# Menu del Administrador
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
                    agregarRuta(grafoDistancias, grafoPrecios)

                case 2:
                    print("----- Ha seleccionado Listar las ciudades/puntos turisticos, distancias y costos ----- ")
                    listarCiudades(grafoDistancias, grafoPrecios)

                case 3:
                    print("----- Ha seleccionado Consultar una ciudad/punto turistico, distancias y costos ----- ")
                    consultarRuta(grafoDistancias, grafoPrecios)

                case 4:
                    print("----- Ha seleccionado Actualizar las ciudades/puntos turisticos ----- ")
                    actualizarRuta(grafoDistancias, grafoPrecios)

                case 5:
                    print("----- Ha seleccionado Eliminar las ciudades/puntos turisticos ----- ")
                    eliminarRuta(grafoDistancias, grafoPrecios)

                case 6:
                    print("----- Ha seleccionado Guardar las ciudades/puntos turisticos, distancias y costos en un archivo ----- ")
                    guardarRutas(grafoDistancias, grafoPrecios)

                case 7:
                    print("--- Saliendo del sistema --- ")
                    break
                case _:
                    print("Elija una opcion valida")
        except ValueError:
            print("Valores invalidos, por favor intente nuevamente")

rolAdmin()