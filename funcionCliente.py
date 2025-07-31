# Bryan Angulo
# Crea dos grafos uno grafoDistancias y grafoprecios a partir de 'rutas.txt'

import os

def cargar_grafos_desde_txt(nombre_archivo):
    grafoDistancias = {}
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

            
    print(f"Grafos cargados correctamente desde '{nombre_archivo}'.")
    return grafoDistancias, grafoPrecios

# En el caso de crear grafos los guarda en 'rutas.txt'


def guardar_grafo_en_txt(grafoDistancias, grafoPrecios, nombre_archivo):
    # Verificar si el archivo ya existe
    if os.path.exists(nombre_archivo):
        respuesta = input(f"El archivo '{nombre_archivo}' ya existe. ¿Deseas sobrescribirlo? (s/n): ")
        if respuesta.lower() != 's':
            print("Operación cancelada.")
            return

    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        rutas_guardadas = set()  # Evita duplicados (bidireccionalidad)

        for origen in grafoDistancias:
            for destino, distancia in grafoDistancias[origen]:
                clave = tuple(sorted((origen, destino)))
                if clave in rutas_guardadas:
                    continue

                # Buscar precio
                precio = None
                for d, p in grafoPrecios.get(origen, []):
                    if d == destino:
                        precio = p
                        break
                if precio is None:
                    for d, p in grafoPrecios.get(destino, []):
                        if d == origen:
                            precio = p
                            break

                if precio is not None:
                    archivo.write(f"Origen: {origen}, Destino: {destino}, Distancia: {distancia}, Precio: {precio}\n")
                    rutas_guardadas.add(clave)

        print(f"Archivo '{nombre_archivo}' guardado correctamente.")

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


# Menu del cliente
def menuCliente():
    seleccion = []
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
            guardarSeleccion(seleccion)
        elif opcion == "0":
            print("\nSaliendo del menu cliente....")
            break
        else:
            print("\nOpción no válida")


#carga las rutas y las hace grafos
archivo = "rutas.txt"
grafoDistancias, grafoDistancias = cargar_grafos_desde_txt(archivo)

def verMapa():
    # Ver mapa de lugares turísticos conectados.
    # Grafo: ciudades y conexiones entre ciudades y lugares turisticos
    #Cargar desde archivo "rutas.txt".
    #funcion 2 de adm
    print("\nMapa de lugares turísticos conectados\n")
    

    for ciudad, conexiones in grafoDistancias.items():
        print(f"Ciudad: {ciudad}")
        if not conexiones:
            print("  (Sin conexiones)")
        else:
            print("     |")
            for destino, distancia in conexiones:
                print(f"     |_______{distancia}_______{destino}")
        print()

    

def consultarRutaOptima():
    #Consultar el costo y la ruta óptima  entre dos ciudades/puntos turísticos y el costo. 
    # Obtener la ruta más corta 
    # Busque mediante un algoritmo de búsqueda (Lineal, Binaria, Interpolación etc.).
    #Pedir lugar de origen y lugar de destino.
    #Utilizar el algoritmo de Dijkstra para encontrar la ruta más económica entre dos ciudades/puntos turísticos .
    #•	BFS (búsqueda de lugares cercanos)
    # •	DFS (exploración de rutas)
    #Heap: para mejorar la eficiencia de Dijkstra (cola de prioridad)

    print("\nRuta óptima entre dos ciudades")
  
    print("\nConsultar la ruta óptima entre dos ciudades\n")

    archivo = "rutas.txt"
    grafoDistancias, grafoPrecios = cargar_grafos_desde_txt(archivo)

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
    #Explorar lugares: organizados jerárquicamente por zonas. (árbol).
    #•	Árbol: jerarquía de zonas o lugares turísticos
    print("\nExplorar lugares")

def seleccionarCiudades(seleccion):
    #Seleccionar ciudades/puntos turísticos a visitar. 
    #Pedir lugar de origen y lugar de destino.
    #(mínimo dos)
    print("\nSeleccionar ciudades a visitar")

def listarSeleccion(seleccion): 
    #Leer datos de ciudades, distancias y costos desde un archivo.
    # Listar la o las ciudades y el costo total(seleccionadas?). 
    # (Ordenar las ciudades /puntos turísticos en base a un algoritmo de ordenamiento 
    # (Burbuja, Inserción, Selección, MergeSort, QuickSort, etc.). 
    print("\nLista de ciudades seleccionadas")  

def actualizarCiudadSeleccion(seleccion):
    # Actualizar la o las ciudades /puntos turísticos (seleccionadas?). 
    print("\nActualizar ciudades seleccionadas ")        

def eliminarCiudadSeleccion(seleccion):
    # Eliminar la o las ciudades /puntos turísticos (seleccionadas?). 
    print("\nEliminar ciudades seleccionadas")   

def guardarSeleccion( seleccion):
    #-	Guadar la selección de ciudades/puntos turísticos 
    # en un archivo “rutas-nombre-del-cliente.txt”
    print("\nGuardar seleccion en archivo")   


menuCliente()