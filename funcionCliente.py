# Bryan Angulo


import os

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
def menuCliente():
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
            guardarSeleccion(seleccion,"Luis")
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

    nombre_archivo = f"rutas-{nombreCliente}.txt"

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



menuCliente()