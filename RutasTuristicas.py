import re
import os

def es_contraseña_segura(contraseña):
    return (re.search(r'[a-z]', contraseña) and
            re.search(r'[A-Z]', contraseña) and
            re.search(r'[0-9]', contraseña))

def registrar_usuario(ruta):
    print("\n--- Registro de Cliente ---")
    nombres = input("Nombres: ").strip()
    identificacion = input("Identificación: ").strip()
    edad = input("Edad: ").strip()
    usuario = input("Correo electrónico: ").strip()
    
    while True:
        contraseña = input("Contraseña (minimo una minuscula, mayuscula y numero): ")
        if es_contraseña_segura(contraseña):
            break
        print("Contraseña no segura. Intenta de nuevo.")

    with open(ruta, 'a') as f:
        f.write(f"{nombres},{identificacion},{edad},{usuario},{contraseña}\n")
    print("Usuario registrado.")

def iniciar_sesion_cliente(ruta):
    print("\n--- Inicio de Sesión Cliente ---")
    usuario = input("Correo electrónico: ").strip()
    contraseña = input("Contraseña: ")

    try:
        with open(ruta, 'r') as f:
            for linea in f:
                datos = linea.strip().split(',')
                if len(datos) == 5 and datos[3] == usuario and datos[4] == contraseña:
                    print("Sesion iniciada.")
                    funcion_cliente(usuario)
                    return True
        print("Usuario o contraseña incorrectos.")
    except FileNotFoundError:
        print("No hay usuarios registrados.")
    return False

def iniciar_sesion_admin():
    print("\n--- Inicio de Sesion Administrador ---")
    usuario = input("Correo electronico: ").strip()
    contraseña = input("Contraseña: ")
    
    # Credenciales de administrador
    if usuario == "administrador@epn.edu.com" and contraseña == "Uz4s4r82":
        print("Sesion de administrador iniciada.")
        funcion_administrador()
        return True
    else:
        print("Credenciales incorrectas.")
        return False

# Lara Marco
# Rol administrador


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
            archivo.write(f"Origen: {ruta['origen']}, Destino: {ruta['destino']}, Distancia: {ruta['distancia']}, Precio: {ruta['precio']} \n")


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



# Crea dos grafos uno grafoDistancias y grafoprecios a partir de 'rutas.txt'
# Crea dos grafos uno grafoDistancias y grafoPrecios a partir de 'rutas.txt'
def cargar_grafos_desde_txt(nombre_archivo):
    grafoDistancias = {}  # inicializa grafos
    grafoPrecios = {}
    rutas_cargadas = set()  # Para evitar duplicados

    if not os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' no existe.")
        return grafoDistancias, grafoPrecios

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            if linea.strip() == "":
                continue

            partes = linea.strip().split(',')
            origen = partes[0].split(":")[1].strip()
            destino = partes[1].split(":")[1].strip()
            distancia = float(partes[2].split(":")[1].strip())
            precio = float(partes[3].split(":")[1].strip())

            clave = tuple(sorted((origen, destino)))
            if clave in rutas_cargadas:
                continue  

            grafoDistancias.setdefault(origen, []).append((destino, distancia))
            grafoDistancias.setdefault(destino, []).append((origen, distancia))

            grafoPrecios.setdefault(origen, []).append((destino, precio))
            grafoPrecios.setdefault(destino, []).append((origen, precio))

            rutas_cargadas.add(clave)

    return grafoDistancias, grafoPrecios


# Algoritmo dijkstra para encontrar ruta mas optima necesita el grafo el inicio y el fin
import heapq

def dijkstra(grafo, inicio, final):
    distancias = {ciudad: float('inf') for ciudad in grafo}
    distancias[inicio] = 0
    anteriores = {ciudad: None for ciudad in grafo}
    heap = [(0, inicio)]

    while heap:
        costo_actual, ciudad_actual = heapq.heappop(heap)

        if ciudad_actual == final:
            break

        for vecino, costo in grafo.get(ciudad_actual, []):
            nuevo_costo = costo_actual + costo
            if nuevo_costo < distancias[vecino]:
                distancias[vecino] = nuevo_costo
                anteriores[vecino] = ciudad_actual
                heapq.heappush(heap, (nuevo_costo, vecino))

    # Reconstruir el camino
    camino = []
    ciudad = final
    while ciudad:
        camino.insert(0, ciudad)
        ciudad = anteriores[ciudad]
    
    return distancias[final], camino


#dfs
def dfs(grafo, nodo, visitados=None):
        if visitados is None:
            visitados = set()  # Usamos set para evitar duplicados
        visitados.add(nodo)
        print(nodo, end="")

        for vecino, _ in grafo.get(nodo, []):  # Desempacamos (vecino, distancia)
            if vecino not in visitados:
                print(" → ", end="")
                dfs(grafo, vecino, visitados)
#dfs modificado buscar todas las rutas posibles
def buscar_rutas_dfs(origen, destino, grafo):
    rutas_encontradas = []

    def dfs_mod(ciudad_actual, destino, camino, visitados):
        visitados.add(ciudad_actual)
        camino.append(ciudad_actual)

        if ciudad_actual == destino:
            rutas_encontradas.append(list(camino))
        else:
            for vecino, _ in grafo.get(ciudad_actual, []):
                if vecino not in visitados:
                    dfs_mod(vecino, destino, camino, visitados)

        camino.pop()
        visitados.remove(ciudad_actual)

    dfs_mod(origen, destino, [], set())
    return rutas_encontradas


#ordenameinto 
# Ordenar rutas por precio usando algoritmo burbuja
def ordenar_por_precio(rutas_info):
    for i in range(len(rutas_info) - 1):
        for j in range(len(rutas_info) - 1 - i):
            if rutas_info[j][2] > rutas_info[j + 1][2]:  # comparando precios
                rutas_info[j], rutas_info[j + 1] = rutas_info[j + 1], rutas_info[j]

# ordenamiento por distancia_total (ascendente)
def ordenar_por_distancia(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j]['distancia'] > lista[j + 1]['distancia']:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]



# Menu del cliente
def menuCliente(nombreLogin):
    while True:
        print(f"\n----------------- Menu Cliente -----------------\n")
        print("1. Ver mapa de lugares turísticos conectados")
        print("2. Consultar la ruta óptima entre dos ciudades")
        print("3. Explorar lugares")
        print("4. Seleccionar ciudades a visitar")
        print("5. Listar la o las  ciudades seleccionadas")
        print("6. Actualizar la o las ciudades  seleccionadas")
        print("7. Eliminar la o las ciudades seleccionadas")
        print("8. Guardar selección de ciudades")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            verMapa()
        elif opcion == "2":
            consultarRutaOptima()
        elif opcion == "3":
            explorarLugares()
        elif opcion == "4":
            seleccionarCiudades(seleccion)
        elif opcion == "5":
            listarSeleccion(seleccion)
        elif opcion == "6":
            actualizarCiudadSeleccion(seleccion)
        elif opcion == "7":
            eliminarCiudadSeleccion(seleccion)
        elif opcion == "8":
            guardarSeleccion(seleccion,nombreLogin)
        elif opcion == "0":
            print("\nSaliendo del menu cliente....")
            break
        else:
            print("\nOpción no válida")


#carga las rutas y las hace grafos
archivo = "rutas.txt"
grafoDistancias, grafoPrecios = cargar_grafos_desde_txt(archivo)

def verMapa():
    # Ver mapa de lugares turísticos conectados.
    # Grafo: ciudades y conexiones entre ciudades y lugares turisticos
    #Cargar desde archivo "rutas.txt".
    print("\n-----------Mapa de lugares turísticos conectados----------------\n")
    

    for ciudad, conexiones in grafoDistancias.items():
        print(f"Ciudad: {ciudad}")
        if not conexiones:
            print("  (Sin conexiones)")
        else:
            print("     |")
            for destino, distancia in conexiones:
                print(f"     |_______{distancia}_(km)______{destino}")
        print()

    

def consultarRutaOptima():
    # Consultar el costo y la ruta óptima  entre dos ciudades y el costo. 
    # Pide el lugar de origen y lugar de destino.
    # Utiliza el algoritmo de Dijkstra para encontrar la ruta más económica o corta entre dos ciudades turísticos .


    print("\n----------------- Ruta óptima entre dos ciudades----------------- ")

    origen = input("Ingrese la ciudad de origen: ").strip()
    destino = input("Ingrese la ciudad de destino: ").strip()

    if origen not in grafoDistancias or destino not in grafoDistancias:
        print("Una o ambas ciudades no existen en el grafo.")
        return

    # Ruta más corta en distancia
    distancia_total, camino_distancia = dijkstra(grafoDistancias, origen, destino)

    # Ruta más económica en precio
    precio_total, camino_precio = dijkstra(grafoPrecios, origen, destino)

    print("\n--- Ruta óptima por distancia ---")
    print("Camino:", " → ".join(camino_distancia))
    print("Distancia total:", distancia_total, "km")

    print("\n--- Ruta más económica ---")
    print("Camino:", " → ".join(camino_precio))
    print("Precio total: $", precio_total)

def explorarLugares():
    #Explorar lugares: organizados jerárquicamente 
    
    print("\n----------------- Explorar ciudades -----------------\n")

    origen = input("Ingrese la ciudad desde donde desea explorar: ").strip()

    if origen not in grafoDistancias:
        print(f"La ciudad '{origen}' no existe en el grafo.")
        return

    print(f"\nExplorando rutas desde: {origen}")
    dfs(grafoDistancias, origen)

#-------------------------------------------------------------------------
seleccion=[]
def seleccionarCiudades(seleccion):
    print("\nSeleccionar ciudades a visitar")
    origen = input("Ingrese la ciudad de origen: ").strip()
    destino = input("Ingrese la ciudad de destino: ").strip()

    if origen not in grafoDistancias or destino not in grafoDistancias:
        print("Una o ambas ciudades no existen en el grafo.")
        return

    # Buscar todas las rutas posibles (DFS modificado)
    rutas_encontradas = buscar_rutas_dfs(origen, destino, grafoDistancias)

    if not rutas_encontradas:
        print(f"No se encontraron rutas posibles de {origen} a {destino}.")
        return

    # Calcular distancia y precio por ruta
    rutas_info = []
    for ruta in rutas_encontradas:
        distancia_total = 0
        precio_total = 0
        for j in range(len(ruta) - 1):
            ciudad_a = ruta[j]
            ciudad_b = ruta[j + 1]

            # Buscar distancia
            for vecino, d in grafoDistancias[ciudad_a]:
                if vecino == ciudad_b:
                    distancia_total += d
                    break

            # Buscar precio
            for vecino, p in grafoPrecios[ciudad_a]:
                if vecino == ciudad_b:
                    precio_total += p
                    break

        rutas_info.append((ruta, distancia_total, precio_total))

    # Ordenar rutas por precio usando función reutilizable
    ordenar_por_precio(rutas_info)

    # Mostrar rutas ordenadas
    print(f"\nSe encontraron {len(rutas_info)} rutas posibles (ordenadas por precio):")
    for i, (ruta, distancia_total, precio_total) in enumerate(rutas_info, start=1):
        print(f"{i}. {' → '.join(ruta)} | Distancia: {distancia_total} km | Precio: ${precio_total:.2f}")

    # Selección de ruta
    while True:
        try:
            eleccion = int(input(f"\nSeleccione el número de la ruta que desea guardar (1-{len(rutas_info)}): "))
            if 1 <= eleccion <= len(rutas_info):
                ruta_elegida, dist_total, prec_total = rutas_info[eleccion - 1]
                seleccion.append({
                    'origen': origen,
                    'destino': destino,
                    'ruta': ruta_elegida,
                    'distancia': dist_total,
                    'precio': prec_total
                })
                print("Ruta guardada exitosamente.")
                break
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")



def listarSeleccion(seleccion): 
    
    print("\nLista de ciudades seleccionadas")  
    if not seleccion:
        print("\nNo hay rutas seleccionadas para mostrar.")
        return

    # Usar función reutilizable para ordenar por distancia
    ordenar_por_distancia(seleccion)

    print("\n--- Rutas seleccionadas ordenadas por distancia ---")
    for i, ruta in enumerate(seleccion, start=1):
        print(f"{i}. {' → '.join(ruta['ruta'])} | Distancia: {ruta['distancia']} km | Precio: ${ruta['precio']:.2f}")


def actualizarCiudadSeleccion(seleccion):
    # Actualizar la o las ciudades /puntos turísticos (seleccionadas?). 
    if not seleccion:
        print("\nNo hay rutas guardadas para actualizar.")
        return

    print("\nRutas guardadas:")
    for i, ruta in enumerate(seleccion, start=1):
        print(f"{i}. {ruta['origen']} → {ruta['destino']} | Ruta: {' → '.join(ruta['ruta'])} | Distancia: {ruta['distancia']} km | Precio: ${ruta['precio']:.2f}")

    try:
        eleccion = int(input(f"\nSeleccione el número de la ruta que desea actualizar (1-{len(seleccion)}): "))
        if eleccion < 1 or eleccion > len(seleccion):
            print("Número fuera de rango.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    # Eliminar la ruta antigua seleccionada
    seleccion.pop(eleccion - 1)

    print("\nPor favor, seleccione una nueva ruta para reemplazar la anterior:")
    # Llamamos a seleccionarCiudades para añadir una nueva ruta a seleccion
    seleccionarCiudades(seleccion)

    print("Actualización completada.") 


def eliminarCiudadSeleccion(seleccion):
    # Eliminar la o las ciudades /puntos turísticos (seleccionadas?). 
    print("\nEliminar ciudades seleccionadas")  
    if not seleccion:
        print("\nNo hay rutas guardadas para eliminar.")
        return

    print("\nRutas guardadas:")
    for i, ruta in enumerate(seleccion, start=1):
        # Corregido nombres claves aquí (punto 3)
        print(f"{i}. {ruta['origen']} → {ruta['destino']} | Ruta: {' → '.join(ruta['ruta'])} | Distancia: {ruta['distancia']} km | Precio: ${ruta['precio']:.2f}")

    try:
        eleccion = int(input(f"\nSeleccione el número de la ruta que desea eliminar (1-{len(seleccion)}): "))
        if eleccion < 1 or eleccion > len(seleccion):
            print("Número fuera de rango.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    ruta_eliminada = seleccion.pop(eleccion - 1)
    print(f"Ruta de {ruta_eliminada['origen']} a {ruta_eliminada['destino']} eliminada exitosamente.")


def guardarSeleccion(seleccion, nombreCliente):
    # - Guardar la selección de ciudades/puntos turísticos 
    # en un archivo “rutas-nombre-del-cliente.txt”
    if not seleccion:
        print("\nNo hay rutas para guardar.")
        return

    if not nombreCliente:
        print("Error: Debe proporcionar un nombre de cliente válido para guardar el archivo.")
        return

    nombre_archivo = f"rutas-{nombreCliente.split()[0]}.txt"


    try:
        with open(nombre_archivo, "w") as archivo:
            for ruta in seleccion:
                linea = (
                    f"Origen: {ruta['origen']}, "
                    f"Destino: {ruta['destino']}, "
                    f"Ruta: {'->'.join(ruta['ruta'])}, "
                    f"Distancia: {ruta['distancia']} km, "
                    f"Precio: ${ruta['precio']:.2f}\n"
                )
                archivo.write(linea)
        print(f"Selección guardada exitosamente en el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")




def funcion_administrador():

    print("\nBienvenido ADMINISTRADOR")
    rolAdmin()

def funcion_cliente(usuario):
    print(f"\nBienvenido {usuario}")
    menuCliente(usuario)






def menu_login(ruta):
    while True:
        print("\n--- Menú Cliente ---")
        print("1. Registrar")
        print("2. Iniciar sesión")
        print("3. Volver")
        opcion = input("Opción: ").strip()

        if opcion == '1':
            registrar_usuario(ruta)
        elif opcion == '2':
            if iniciar_sesion_cliente(ruta):
                break
        elif opcion == '3':
            break
        else:
            print("Opción inválida.")

def main():
    ruta = "usuarios.txt"
  
    while True:
        print("\n=== Menú Principal ===")
        print("1. Administrador")
        print("2. Cliente")
        print("3. Salir")
        opcion = input("Opción: ").strip()

        if opcion == '1':
            iniciar_sesion_admin()
        elif opcion == '2':
            menu_login(ruta)
        elif opcion == '3':
            print("Hasta pronto.")
            break
        else:
            print("Opción inválida.")

main()